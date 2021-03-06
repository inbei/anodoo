# -*- coding: utf-8 -*-
{
    'name': "支付",

    'summary': """
        支付管理
    """,

    'description': """
        支付管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-pay",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'anodoo_sale', 'anodoo_lead'],

    # always loaded
    'data': [
        'data/pay_data.xml',
        'security/pay_security.xml',
        'security/ir.model.access.csv',
        'views/pay_views.xml',
        'views/pay_menu.xml',
        'views/pay_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/pay_demo.xml',
    ],
}