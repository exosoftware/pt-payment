##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exosoftware.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author
{
    "name": "Ifthenpay Payment Acquirer",
    "category": "Accounting/Payment Acquirers",
    "sequence": 390,
    "summary": "Payment Acquirer: Ifthenpay Implementation",
    "version": "15.0.2.1.0",
    "author": "Exo Software",
    "website": "https://exosoftware.pt",
    "depends": ["payment_portugal"],
    "data": [
        "views/payment_views.xml",
        "views/payment_ifthenpay_templates.xml",
        "data/payment_acquirer_data.xml",
    ],
    "installable": True,
    "application": True,
    "uninstall_hook": "uninstall_hook",
    "license": "OPL-1",
}
