from datetime import datetime

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    print_date = fields.Datetime('Print Date')

    def action_invoice_print(self):
        res = super(AccountMove, self).action_invoice_print()
        if not self.print_date:
            self.write({
                'print_date': datetime.now()
            })
        return res

    def copy(self, default=None):
        default = dict(default or {})
        default['print_date'] = None
        return super(AccountMove, self).copy(default=default)