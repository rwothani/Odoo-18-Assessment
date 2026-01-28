from odoo import models, fields, api, _


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
            ("rfq_sent", "RFQs Sent"),
            ("done", "Done"),
        ],
        default="draft",
    )

    line_ids = fields.One2many(
        "purchase.request.line",
        "request_id",
        string="Request Lines",
    )

    bid_ids = fields.One2many(
        "purchase.request.bid",
        "request_id",
        string="Vendor Bids",
    )

    # --------------------------------------------------
    # BUTTON ACTIONS
    # --------------------------------------------------

    def action_view_bids(self):
        """Open vendor bids related to this purchase request"""
        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "name": _("Vendor Bids"),
            "res_model": "purchase.request.bid",
            "view_mode": "list,form",
            "domain": [("request_id", "=", self.id)],
            "context": {
                "default_request_id": self.id,
            },
        }

    def action_request_rfq(self):
        """
        Simulate RFQ sending.
        Later this can be extended to real purchase.order RFQs.
        """
        for request in self:
            if not request.line_ids:
                raise ValueError("You must add at least one request line.")

            request.state = "rfq_sent"

        return True