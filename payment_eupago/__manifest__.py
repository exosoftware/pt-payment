##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exosoftware.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author
{
    "name": "Eupago Payment Acquirer",
    "category": "Accounting/Payment Acquirers",
    "sequence": 391,
    "summary": "Payment Acquirer: Eupago Implementation",
    "version": "14.0.2.2.0",
    "author": "Exo Software",
    "website": "https://exosoftware.pt",
    "depends": ["payment_portugal"],
    "data": [
        "views/payment_views.xml",
        "views/payment_eupago_templates.xml",
        "data/payment_acquirer_data.xml",
    ],
    "installable": True,
    "application": True,
    "post_init_hook": "create_missing_journal_for_acquirers",
    "uninstall_hook": "uninstall_hook",
    "license": "OPL-1",
}
