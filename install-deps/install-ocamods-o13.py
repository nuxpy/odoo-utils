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
repositories = ['account-closing', 'account-consolidation', 'account-financial-tools',
    'account-payment', 'account-reconcile', 'bank-payment', 'calendar', 'connector-ecommerce',
    'crm', 'e-commerce', 'hr', 'hr-expense', 'hr-holidays', 'l10n-spain', 'vertical-hotel',
    'web', 'website', 'website-cms', 'website-themes'
]

os.system('apt-get install aptitude')
os.system('aptitude update')
os.system('aptitude -yr install %s' % (paqrepdeb))

if not os.path.exists('oca'):
    os.mkdir('oca')

for r in repositories:
    os.system('cd oca; git clone -b %s %s%s' % (branch, oca, r))