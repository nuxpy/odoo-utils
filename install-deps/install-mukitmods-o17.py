# -*- coding: utf-8 -*-
''' This script gets modules from muk-it repository on GitHub to version 17
    * At first time installs "aptitude" as main manager of installations
    * You can use it on Debian/Ubuntu as root user or sudo way:
    
        chmod +x install-mukitmods-o16.py
        ./install-mukitmods-o16.py

'''
import os, re, sys

paqrepdeb = "git"
mukiturl = 'https://github.com/muk-it/'
branch = '17.0'
repositories = [
    'odoo-modules',
    'muk_web',
    'muk_dms',
    'muk_bundles',
    'muk_base',
    'muk_docs',
    'muk_website',
    'muk_misc',
    'muk_quality',
    'muk_tests',
]

if not os.path.exists('mukit'):
    os.mkdir('mukit')
    for r in repositories:
        os.system('cd mukit; git clone -b %s %s%s' % (branch, mukiturl, r))
else:
    for r in repositories:
        if not os.path.exists('mukit/%s' % r):
            os.mkdir('mukit/%s' % r)
            os.system('cd mukit; git clone -b %s %s%s; cd -' % (branch, mukiturl, r))
        else:
            os.system('cd mukit/%s; git pull; cd -' % (r))
