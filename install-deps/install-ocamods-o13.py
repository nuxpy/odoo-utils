#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' This script gets modules from OCA repository on GitHub to version 13
    * At first time installs "aptitude" as main manager of installations
    * You can use it on Debian/Ubuntu as root user or sudo way:
    
        chmod +x install-ocamods-o13.py
        ./install-ocamods-o13.py

'''
import os, re, sys

paqrepdeb = "git"
oca = 'https://github.com/OCA/'
branch = '13.0'
repositories = [
    'account-closing',
    'account-consolidation',
    'account-financial-tools',
    'account-payment',
    'account-reconcile',
    'bank-payment',
    'brand',
    'calendar',
    'connector-ecommerce',
    'crm',
    'e-commerce',
    'helpdesk',
    'hr',
    'hr-attendance',
    'hr-expense',
    'hr-holidays',
    'l10n-spain',
    'project',
    'stock-logistics-barcode',
    'stock-logistics-reporting',
    'stock-logistics-tracking',
    'stock-logistics-transport',
    'stock-logistics-warehouse',
    'stock-logistics-workflow',
    'timesheet',
    'vertical-hotel',
    'web',
    'website',
    'website-cms',
    'website-themes'
]

os.system('apt-get install aptitude')
os.system('aptitude update')
os.system('aptitude -yr install %s' % (paqrepdeb))

if not os.path.exists('oca'):
    os.mkdir('oca')
    for r in repositories:
        os.system('cd oca; git clone -b %s %s%s' % (branch, oca, r))
else:
    for r in repositories:
        os.system('cd oca/%s; git pull %s%s; cd -' % (r, oca, r))
