from odoo import models, fields


class PurchaseRequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase Request"

    name = fields.Char(string="Reference", required=True, default="New")
    requested_by = fields.Many2one(
        "res.users",
        string="Requested By",
        default=lambda self: self.env.user,
    )
    date_request = fields.Date(
        string="Request Date",
        default=fields.Date.context_today,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("prepared", "Prepared"),
            ("sent", "Sent"),
        ],
        default="draft",
    )
    line_ids = fields.One2many(
        "purchase.request.line",
        "request_id",
        string="Request Lines",
    )