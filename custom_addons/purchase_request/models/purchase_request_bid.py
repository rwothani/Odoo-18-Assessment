from odoo import models, fields


class PurchaseRequestBid(models.Model):
    _name = "purchase.request.bid"
    _description = "Purchase Request Vendor Bid"

    request_id = fields.Many2one(
        "purchase.request",
        string="Purchase Request",
        required=True,
        ondelete="cascade",
    )

    vendor_id = fields.Many2one(
        "res.partner",
        string="Vendor",
        required=True,
        domain=[("supplier_rank", ">", 0)],
    )

    price_total = fields.Float(
        string="Quoted Price",
        required=True,
    )

    delivery_days = fields.Integer(
        string="Delivery Lead Time (Days)",
        required=True,
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

    def action_accept_bid(self):
        for bid in self:
            bid.request_id.bid_ids.write({
                "state": "rejected",
                "is_winner": False,
            })
            bid.write({
                "state": "accepted",
                "is_winner": True,
            })