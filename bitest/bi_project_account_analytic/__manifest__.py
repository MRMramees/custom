# -*- coding: utf-8 -*-
{
    'name': "bi_project_account_analytics",

    
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project','account','purchase'],

    # always loaded
    'data': ['views/purchase_views_inherit.xml'],

    'application': True
}
