from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PurchaseRfqBid(models.Model):
    _name = "purchase.rfq.bid"
    _description = "RFQ Vendor Bid"
    _order = "rfq_id, vendor_id"

    rfq_id = fields.Many2one(
        "purchase.order",
        string="RFQ",
        required=True,
        ondelete="cascade",
        index=True,
    )

    vendor_id = fields.Many2one(
        "res.partner",
        string="Vendor",
        required=True,
        domain=[("supplier_rank", ">", 0)],
    )

    price_total = fields.Monetary(
        string="Quoted Total",
        required=False,
        default=0.0,
        currency_field="currency_id",
    )

    currency_id = fields.Many2one(
        related="rfq_id.currency_id",
        readonly=True,
    )

    delivery_days = fields.Integer(
        string="Delivery Lead Time (Days)",
        required=True,
        default=14,
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("submitted", "Submitted"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
        ],
        default="draft",
        string="Status",
        tracking=True,
    )

    is_winner = fields.Boolean(
        string="Winning Bid",
        default=False,
        copy=False,
    )

    purchase_order_id = fields.Many2one(
        "purchase.order",
        string="Confirmed PO",
        readonly=True,
        copy=False,
    )

    def action_submit(self):
        self.write({"state": "submitted"})

    def action_accept(self):
        self.ensure_one()

        if self.state != "submitted":
            raise UserError(_("Only submitted bids can be accepted."))

        # Reject others
        self.rfq_id.bid_ids.filtered(lambda b: b != self).write({
            "state": "rejected",
            "is_winner": False,
        })

        self.write({
            "state": "accepted",
            "is_winner": True,
        })

    def action_create_po(self):
        self.ensure_one()

        if not self.is_winner:
            raise UserError(_("Only the winning bid can generate a Purchase Order."))

        if self.purchase_order_id:
            return self.purchase_order_id.get_formview_action()

        po = self.rfq_id.copy({
            "partner_id": self.vendor_id.id,
            "state": "draft",
            "origin": f"{self.rfq_id.name} - Winning bid {self.vendor_id.name}",
        })

        self.purchase_order_id = po.id
        self.rfq_id.write({"state": "done"})

        return po.get_formview_action()