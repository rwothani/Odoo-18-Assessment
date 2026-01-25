from odoo import models, fields


class PurchaseBid(models.Model):
    _name = "purchase.bid"
    _description = "Vendor Bid"

    rfq_id = fields.Many2one(
        "purchase.order",
        string="RFQ",
        required=True,
        ondelete="cascade",
    )
    vendor_id = fields.Many2one(
        "res.partner",
        string="Vendor",
        required=True,
        domain=[("supplier_rank", ">", 0)],
    )
    price_total = fields.Monetary(
        string="Bid Amount",
        required=True,
    )
    currency_id = fields.Many2one(
        "res.currency",
        related="rfq_id.currency_id",
        readonly=True,
    )
    delivery_days = fields.Integer(
        string="Delivery Days",
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("submitted", "Submitted"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
        ],
        default="draft",
    )
    is_winner = fields.Boolean(
        string="Winning Bid",
        default=False,
    )