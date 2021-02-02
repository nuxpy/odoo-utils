#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' This script gets dependencies of Odoo to version 11
    * At first time installs "aptitude" as main manager of installations
    * You can use it on Debian/Ubuntu as root user or sudo way:
    
        chmod +x install-deps-o11.py
        ./install-deps-o11.py

'''
import os
import re
import sys

''' Debian packages
'''
paqrepdeb = ['libxrender1','libfontconfig1','fontconfig','postgresql-9.6','python3-babel','python3-dateutil','python3-decorator','python3-docutils','python3-feedparser','python3-gevent','python3-html2text','python3-jinja2','python3-lxml','python3-mako','python3-mock','python3-ofxparse','python3-passlib','python3-pil','python3-psutil','python3-psycopg2','python3-pydot','python3-pyparsing','python3-pypdf2','python3-reportlab','python3-serial','python3-tz','python3-usb','python3-vatnumber','python3-werkzeug','python3-xlsxwriter','python3-yaml','node-less','postgresql-client','python3-suds','python3-pip','wkhtmltopdf','xfonts-75dpi']

os.system('apt-get install aptitude')
os.system('aptitude update')
for p in paqrepdeb:
    os.system('aptitude -yr install %s' % p)

''' Download wkhtmltopdf for Debian Buster Amd64 processor
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
    os.system('pip3 install --upgrade %s' % (i))
