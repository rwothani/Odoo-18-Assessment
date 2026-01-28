{
    "name": "Purchase Request with Multi-Vendor RFQ and Bids",
    "version": "1.0",
    "category": "Purchases",
    "summary": "Allows employees to create purchase requests, procurement to create multi-vendor RFQs, receive bids, and select winner",
    "author": "Rachel Anirwoth (Assignment)",
    "depends": ["purchase"],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",                    
        "views/purchase_request_views.xml",
        "views/purchase_order_views.xml",
        "views/rfq_bid_views.xml",
        "views/purchase_request_menu.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}