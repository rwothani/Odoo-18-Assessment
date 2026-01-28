from odoo import models, fields


class PurchaseRequestLine(models.Model):
    _name = "purchase.request.line"
    _description = "Purchase Request Line"

    request_id = fields.Many2one(
        "purchase.request",
        required=True,
        ondelete="cascade",
    )

    product_id = fields.Many2one(
        "product.product",
        string="Product",
        required=True,
    )

    quantity = fields.Float(
        string="Quantity",
        required=True,
        default=1.0,
    )

    uom_id = fields.Many2one(
        "uom.uom",
        string="Unit of Measure",
        related="product_id.uom_po_id",
        readonly=False,
        store=True,
    )