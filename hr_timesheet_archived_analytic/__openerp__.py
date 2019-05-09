# -*- coding: utf-8 -*-
# Copyright 2019 Coop IT Easy SCRLfs
#     - Rémy Taymans <remy@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Hr Timesheet Archived Analytic',
    'description': """
        Hide archived analytic account in the timesheet form.""",
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Coop IT Easy SCRLfs',
    'website': 'https://coopiteasy.be',
    'depends': [
        'hr_timesheet_sheet',
    ],
    'data': [
        'views/hr_timesheet_sheet.xml',
    ],
}
