# Copyright 2026 Exo Software
import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

# The payment methods this module used to ship, and the Odoo ones that replace
# them. Identified by xmlid, not by code: ours and Odoo's MB WAY method share
# the code `mbway`, so the code alone cannot tell them apart.
METHOD_REPLACEMENTS = [
    ("payment_portugal.payment_icon_mb", "payment.payment_method_multibanco"),
    ("payment_portugal.payment_icon_mbway", "payment.payment_method_mbway"),
]


@openupgrade.migrate()
def migrate(env, version):
    for legacy_xmlid, target_xmlid in METHOD_REPLACEMENTS:
        legacy = env.ref(legacy_xmlid, raise_if_not_found=False)
        target = env.ref(target_xmlid, raise_if_not_found=False)
        if not legacy or not target or legacy == target:
            continue
        _replace_payment_method(env, legacy, target)


def _replace_payment_method(env, legacy, target):
    """Move every reference to our own payment method onto Odoo's, then drop ours."""
    _logger.info(
        "Replacing payment method %s (%s) by %s (%s)",
        legacy.code,
        legacy.id,
        target.code,
        target.id,
    )
    params = {"legacy": legacy.id, "target": target.id}

    for table in ("payment_transaction", "payment_token"):
        openupgrade.logged_query(
            env.cr,
            f"""
            UPDATE {table}
            SET payment_method_id = %(target)s
            WHERE payment_method_id = %(legacy)s
            """,
            params,
        )

    openupgrade.logged_query(
        env.cr,
        """
        UPDATE payment_method
        SET primary_payment_method_id = %(target)s
        WHERE primary_payment_method_id = %(legacy)s
        """,
        params,
    )

    # Providers are a many2many: move the links Odoo's method does not have
    # yet, then drop what is left over so the delete finds nothing attached.
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE payment_method_payment_provider_rel rel
        SET payment_method_id = %(target)s
        WHERE payment_method_id = %(legacy)s
          AND NOT EXISTS (
              SELECT 1
              FROM payment_method_payment_provider_rel other
              WHERE other.payment_method_id = %(target)s
                AND other.payment_provider_id = rel.payment_provider_id
          )
        """,
        params,
    )
    openupgrade.logged_query(
        env.cr,
        """
        DELETE FROM payment_method_payment_provider_rel
        WHERE payment_method_id = %(legacy)s
        """,
        params,
    )

    env.invalidate_all()
    legacy.unlink()
