# -*- coding: utf-8 -*-
{
    'name': "bi_clinic",
 
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','product','stock','account'],

    'data': [  
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'reports/lab_test_report.xml',
        'reports/reports.xml',
        'views/prescription_views.xml',
        # 'views/account_invoice_view_inherit.xml',
        'views/lab_test_result_views.xml',
        'views/lab_test_request_views.xml',
        'views/patient_medicament_views.xml',
        'views/patient_disease_views.xml',
        'views/appointments_views.xml',
        'views/physician_info_views.xml',
        'views/medicaments_views.xml',
        'views/medicament_dosage_frequency_views.xml',
        'views/medicament_dose_units_views.xml',
        'views/medicament_admin_routes_views.xml',
        'views/medicament_form_views.xml',
        'views/medicament_category_views.xml',
        'views/occupation_views.xml',
        'views/patient_info_views.xml',
        'views/medical_specialities_views.xml',
        'views/genetic_risks_views.xml',
        'views/patients_views.xml',
        'views/disease_sub_category_views.xml',
        'views/disease_main_category_views.xml',     
        'views/disease_names_views.xml',
        'views/lab_test_type_views.xml',
        'views/lab_test_units_views.xml',
        'views/bi_clinic_menus.xml',
        ],
    
    'application': True
}