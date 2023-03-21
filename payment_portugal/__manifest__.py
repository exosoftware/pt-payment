##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exosoftware.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author
{
    "name": "Payment Acquirer Portugal",
    "category": "Accounting/Payment Acquirers",
    "summary": "A base module for portuguese payment methods",
    "version": "14.0.2.1.0",
    "author": "Exo Software",
    "website": "https://exosoftware.pt",
    "depends": ["website_sale", "l10n_pt"],  # TODO: replace website_sale -> sale
    "data": [
        "security/ir.model.access.csv",
        "data/payment_icon_data.xml",
        "data/ir_cron.xml",
        "views/assets.xml",
        "views/report_templates.xml",
        "views/report_invoice.xml",
        "views/report_sale_order.xml",
        "views/payment_views.xml",
        "views/account_move_views.xml",
        "views/res_partner_views.xml",
        "views/payment_templates.xml",
        "views/payment_mbway_templates.xml",
        "wizard/account_generate_multibanco_views.xml",
    ],
    "installable": True,
    "application": False,
    "license": "OPL-1",
}
