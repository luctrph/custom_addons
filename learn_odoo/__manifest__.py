# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo learn',
    'version': '1.0',
    'category': 'Other',
    'summary': 'Odoo learn',
    'description': """
        Odoo learn
    """,
    'depends': [],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/employee_view.xml',
        'views/employee_department_view.xml',
        'views/car_view.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
