#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' This script gets dependencies of Odoo to version 13
    * At first time installs "aptitude" as main manager of installations
    * You can use it on Debian/Ubuntu as root user or sudo way:
    
        chmod +x install-deps-o13.py
        ./install-deps-o13.py

'''
import os, re, sys

paqrepdeb = "python3-babel python3-dateutil python3-decorator python3-docutils python3-feedparser python3-gevent python3-html2text python3-jinja2 python3-lxml python3-mock python3-ofxparse python3-passlib python3-pil python3-psutil python3-psycopg2 python3-pydot python3-pyparsing python3-pypdf2 python3-reportlab python3-serial python3-tz python3-usb python3-vatnumber python3-werkzeug python3-xlsxwriter python3-libsass python3-suds xvfb python3-pip python3-mako python3-xlrd python3-polib python3-qrcode python3-vobject python3-zeep postgresql-11 wkhtmltopdf"

os.system('apt-get install aptitude')
os.system('aptitude update')
os.system('aptitude -yr install %s' % (paqrepdeb))

paqreppip = ['xlwt','PyPDF2','phonenumbers','pyOpenSSL','setuptools','cryptography',
    'cffi','six','pycparser','client','num2words','flanker','xlrd']

# Actualiza dependencias
for i in paqreppip:
    os.system('pip3 install --upgrade %s' % (i))
