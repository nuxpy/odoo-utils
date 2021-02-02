#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' This script gets dependencies of Odoo to version 10
    * At first time installs "aptitude" as main manager of installations
    * You can use it on Debian/Ubuntu as root user or sudo way:
    
        chmod +x install-deps-o10.py
        ./install-deps-o10.py
'''
import os
import re
import sys

''' Debian packages
'''
paqrepdeb = ['adduser','node-less','postgresql-client','python','python-babel','python-dateutil','python-decorator','python-docutils','python-feedparser','python-imaging','python-jinja2','python-ldap','python-libxslt1','python-lxml','python-mako','python-mock','python-openid','python-passlib','python-psutil','python-psycopg2','python-pychart','python-pydot','python-pyparsing','python-pypdf','python-reportlab','python-requests','python-suds','python-tz','python-vatnumber','python-vobject','python-werkzeug','python-xlsxwriter','python-xlwt','python-yaml','wkhtmltopdf','python-pip','numpy','xfonts-75dpi']

os.system('apt-get install aptitude')
os.system('aptitude update')
for i in paqrepdeb:
    os.system('aptitude -yr install %s' % (paqrepdeb))


''' Download wkhtmltopdf
'''
wkh2pdf = 'wkhtmltox_0.12.6-1.buster_amd64.deb'
url_html2pdf = 'https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/%s' % wkh2pdf
os.system('wget -c %s' % url_html2pdf)
os.system('dpkg -i %s' % wkh2pdf)

''' PIP packages
'''
paqreppip = ['xlwt','PyPDF2','phonenumbers','pyOpenSSL','setuptools','cryptography',
  'cffi','six','pycparser','client','num2words','flanker','xlrd']
for i in paqreppip:
    os.system('pip install --upgrade %s' % (i))
