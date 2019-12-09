# -*- coding: utf-8 -*-
# Copyright 2019 Coop IT Easy SCRLfs
#     Houssine Bakkali <houssine@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Purchase order status",
    'summary': """
        This module implements new fields and modify the invoice_status in
        order to give a better view on the purchase order status.
    """,
    'author': 'Coop IT Easy SCRLfs',
    'website': 'www.coopiteasy.be',
    'category': 'Purchase Management',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['purchase'],
    'data': [
        'views/purchase_view.xml',
    ],
}
