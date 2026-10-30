# Copyright 2026 Exo Software
import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    """Unarchive the Odoo payment methods our providers now point at.

    Odoo ships Multibanco and MB WAY archived and only unarchives them for the
    providers that declare them as a default, which `_activate_default_pms`
    does. The pre-migration moved the provider links onto Odoo's records, so
    running it now brings the methods back for the providers already in use.
    """
    # Not `get_mb_providers()`: this runs while `payment_portugal` itself is
    # being loaded, so the provider modules that fill that list are not in the
    # registry yet. `pt_pay_method` belongs to this module and is always there.
    providers = env["payment.provider"].search(
        [("pt_pay_method", "!=", False), ("state", "!=", "disabled")]
    )
    if not providers:
        return
    _logger.info("Activating the PT payment methods of %s", providers.mapped("name"))
    providers._activate_default_pms()
