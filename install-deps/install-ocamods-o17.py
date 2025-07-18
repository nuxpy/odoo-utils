# -*- coding: utf-8 -*-
''' This script gets modules from OCA repository on GitHub to version 13
    * At first time installs "aptitude" as main manager of installations
    * You can use it on Debian/Ubuntu as root user or sudo way:
    
        chmod +x install-ocamods-o16.py
        ./install-ocamods-o16.py

'''
import os, re, sys

paqrepdeb = "git"
ocaurl = 'https://github.com/OCA/'
branch = '17.0'
repositories = [
    'account-analytic',
    'account-budgeting',
    'account-closing',
    'account-consolidation',
    'account-financial-reporting',
    'account-financial-tools',
    'account-fiscal-rule',
    'account-invoice-reporting',
    'account-invoicing',
    'account-payment',
    'account-reconcile',
    'bank-payment',
    'bank-statement-import',
    'brand',
    'calendar',
    'commission',
    'connector-accountedge',
    'connector-cmis',
    'connector-ecommerce',
    'connector-infor',
    'connector-jira',
    'connector-lengow',
    'connector-lims',
    'connector-odoo2odoo',
    'connector-prestashop',
    'connector-redmine',
    'connector-sage',
    'connector-salesforce',
    'connector-spscommerce',
    'connector-woocommerce',
    'crm',
    'delivery-carrier',
    'dms',
    'e-commerce',
    'e-learning',
    'edi',
    'fleet',
    'helpdesk',
    'hr',
    'hr-attendance',
    'hr-expense',
    'hr-holidays',
    'infrastructure',
    'knowledge',
    'l10n-spain',
    'margin-analysis',
    'multi-company',
    'partner-contact',
    'payroll',
    'pos',
    'project',
    'purchase-reporting',
    'purchase-workflow',
    'queue',
    'report-print-send',
    'reporting-engine',
    'sale-blanket',
    'sale-channel',
    'sale-financial',
    'sale-prebook',
    'sale-promotion',
    'sale-reporting',
    'sale-workflow',
    'search-engine',
    'server-auth',
    'server-backend',
    'server-brand',
    'server-env',
    'server-tools',
    'server-ux',
    'shift-planning',
    'spreadsheet',
    'stock-logistics-barcode',
    'stock-logistics-reporting',
    'stock-logistics-tracking',
    'stock-logistics-transport',
    'stock-logistics-warehouse',
    'stock-logistics-workflow',
    'survey',
    'timesheet',
    'vertical-agriculture',
    'vertical-association',
    'vertical-community',
    'vertical-construction',
    'vertical-cooperative-supermarket',
    'vertical-education',
    'vertical-hotel',
    'vertical-isp',
    'vertical-medical',
    'vertical-realestate',
    'vertical-rental',
    'web',
    'website',
    'website-cms',
    'website-themes',
    'wms',
]

if not os.path.exists('oca'):
    os.mkdir('oca')
    for r in repositories:
        os.system('cd oca; git clone -b %s %s%s' % (branch, ocaurl, r))
else:
    for r in repositories:
        if not os.path.exists('oca/%s' % r):
            os.mkdir('oca/%s' % r)
            os.system('cd oca; git clone -b %s %s%s; cd -' % (branch, ocaurl, r))
        else:
            os.system('cd oca/%s; git pull; cd -' % (r))
