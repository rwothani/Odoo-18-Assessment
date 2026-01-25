{
    "name": "Purchase Request & Multi-Vendor RFQ",
    "version": "1.0",
    "category": "Purchases",
    "summary": "Purchase Requests with Multi-Vendor RFQs and Bids",
    "author": "Rachel Anirwoth (Assignment)",
    "depends": ["purchase"],
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_request_views.xml",
        "views/purchase_request_menu.xml",
    ],
    "installable": True,
    "application": False,
}
