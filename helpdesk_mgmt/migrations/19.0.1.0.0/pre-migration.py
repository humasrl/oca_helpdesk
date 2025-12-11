# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def migrate(cr, version):
    """Migration script from Odoo 18 to Odoo 19.

    This module is already compatible with Odoo 19:
    - XML views use modern syntax (direct invisible= instead of attrs)
    - No deprecated states attribute in field definitions
    - Controllers use type="http" (no type='json' routes)
    - JavaScript uses modern ESM/OWL patterns

    No database changes required for this migration.
    """
    if not version:
        return
