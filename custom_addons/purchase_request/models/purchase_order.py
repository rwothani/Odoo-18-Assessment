from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # Override the base partner_id to make it optional (for multi-vendor RFQs)
    partner_id = fields.Many2one(
        'res.partner',
        string='Vendor',
        required=False,  # ← Key change: optional for RFQs from purchase request
        readonly=[('state', 'in', ['purchase', 'done'])],
        change_default=True,
        tracking=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )

    purchase_request_id = fields.Many2one(
        "purchase.request",
        string="Source Purchase Request",
        readonly=True,
        index=True,
    )

    vendor_ids = fields.Many2many(
        "res.partner",
        string="Invited Vendors",
        domain=[("supplier_rank", ">", 0)],
        help="Vendors invited to submit bids for this RFQ",
    )

    bid_ids = fields.One2many(
        "purchase.rfq.bid",
        "rfq_id",
        string="Vendor Bids",
    )

    def create_bid_records(self):
        """Create placeholder bid records for all invited vendors that don't have one yet."""
        self.ensure_one()

        if not self.vendor_ids:
            raise UserError(_("No vendors invited yet. Please add at least one vendor."))

        Bid = self.env["purchase.rfq.bid"]
        existing = set(self.bid_ids.mapped("vendor_id").ids)

        created_count = 0
        for vendor in self.vendor_ids:
            if vendor.id not in existing:
                Bid.create({
                    "rfq_id": self.id,
                    "vendor_id": vendor.id,
                    "state": "draft",
                })
                created_count += 1

        if created_count == 0:
            raise UserError(_("Bid records already exist for all invited vendors."))

        return {
            "type": "ir.actions.act_window",
            "res_model": "purchase.order",
            "view_mode": "form",
            "res_id": self.id,
            "target": "current",
        }

    @api.constrains('partner_id', 'state')
    def _check_partner_for_sent(self):
        for order in self:
            if order.state in ['sent', 'purchase'] and not order.partner_id:
                raise ValidationError(_("A vendor must be selected before sending or confirming the RFQ."))