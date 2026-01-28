from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PurchaseRequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase Request"
    _order = "date_request desc, id desc"

    name = fields.Char(
        string="Reference",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _("New"),
    )

    requested_by = fields.Many2one(
        "res.users",
        string="Requested By",
        default=lambda self: self.env.user,
        readonly=True,
    )

    date_request = fields.Date(
        string="Request Date",
        default=fields.Date.context_today,
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("rfq_created", "RFQ Created"),
            ("done", "Done"),
        ],
        default="draft",
        string="Status",
        tracking=True,
    )

    line_ids = fields.One2many(
        "purchase.request.line",
        "request_id",
        string="Products",
        copy=True,
    )

    rfq_ids = fields.One2many(
        "purchase.order",
        "purchase_request_id",
        string="Generated RFQs",
        readonly=True,
        copy=False,
    )

    @api.model
    def create(self, vals):
        if vals.get("name", _("New")) == _("New"):
            vals["name"] = self.env["ir.sequence"].next_by_code("purchase.request") or _("New")
        return super().create(vals)

    def action_create_rfq(self):
        self.ensure_one()
        if not self.line_ids:
            raise UserError(_("Add at least one product line."))

        rfq = self.env['purchase.order'].create({
            
            'purchase_request_id': self.id,
            'origin': self.name,
            'date_order': fields.Date.today(),
            'state': 'draft',
        })

       

        # Copy lines
        for line in self.line_ids:
            self.env['purchase.order.line'].create({
                'order_id': rfq.id,
                'product_id': line.product_id.id,
                'product_qty': line.quantity,
                'product_uom': line.uom_id.id,
                'name': line.product_id.name or 'No description',
            })

        self.state = 'rfq_created'

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'form',
            'res_id': rfq.id,
            'target': 'current',
        }