from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    purchase_request_id = fields.Many2one(
        "purchase.request",
        string="Purchase Request",
    )
    bid_ids = fields.One2many(
        "purchase.bid",
        "rfq_id",
        string="Vendor Bids",
    )