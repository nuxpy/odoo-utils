#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' otoolsdev
'''
import os
import sys
import re
import optparse
from olibdevs import olibdevs


def createapp(name_app=''):
    o = olibdevs()
    if len(name_app):
        name_mod = name_app.lower().strip() if re.match('(\w|\w_\w)', name_app, re.I) else ''
        if name_mod:
            if o.otreebuilder(name_mod) == True:
                o.ofilesbuilder(name_mod)
            else:
                return False
            os.system('chmod 755 -R %s' % name_mod)
        else:
            print ("Use '--app my_name_app' to create a new app.")
            return False
    else:
        print ("There is not app or name to create an Odoo app.")
        print ("Use '--app my_name_app' to create a new app.")
        return False
    return True

def createmodel(get_model='', get_mode=''):
    o = olibdevs()
    if get_mode == 'new':
        mode = 'name'
    elif get_mode == 'inherit':
        mode = 'inherit'
    else:
        print ("Use the following options to create a model:\n")
        print ("\t--object new model.model\n")
        print ("\t--object inherit model.model\n")
        return False
    if get_model:
        model_file = '%s.py' % get_model.lower().strip().replace('.','_')
        mnl = [i.capitalize() for i in get_model.split('.')]
        class_name = '%s%s' % (mnl[0], mnl[1])
        content = o.contentmodel(class_name, mode, get_model)
        if os.path.isfile(model_file):
            if sys.version_info.major < 3:
                yn = raw_input("There is a file. Do you want to overwrite it? (y/n) ")
            else:
                yn = input("There is a file. Do you want to overwrite it? (y/n) ")
            if yn == 'y':
                model_file_w = open(model_file, 'w')
                model_file_w.write(content)
                model_file_w.close()
            else:
                return False
        else:
            model_file_w = open(model_file, 'w')
            model_file_w.write(content)
            model_file_w.close()
    return True

def createmodelwizard(get_model='', get_mode=''):
    o = olibdevs()
    if get_mode == 'new':
        mode = 'name'
    elif get_mode == 'inherit':
        mode = 'inherit'
    else:
        print ("Use the following options to create a model:\n")
        print ("\t--wizard new model.model\n")
        print ("\t--wizard inherit model.model\n")
        return False
    if get_model:
        model_file = '%s.py' % get_model.lower().strip().replace('.','_')
        mnl = [i.capitalize() for i in get_model.split('.')]
        class_name = '%s%s' % (mnl[0], mnl[1])
        content = o.contentmodelwizard(class_name, mode, get_model)
        if os.path.isfile(model_file):
            if sys.version_info.major < 3:
                yn = raw_input("There is a file. Do you want to overwrite it? (y/n) ")
            else:
                yn = input("There is a file. Do you want to overwrite it? (y/n) ")
            if yn == 'y':
                model_file_w = open(model_file, 'w')
                model_file_w.write(content)
                model_file_w.close()
            else:
                return False
        else:
            model_file_w = open(model_file, 'w')
            model_file_w.write(content)
            model_file_w.close()
    return True

def createview(mode='', model='', views=''):
    o = olibdevs()
    if mode and model and views:
        name_view_xml = '%s_view.xml' % model.replace('.','_').lower()
        view_id = name_view_xml.split('.')[0]
        view_name = model
        model_name = model
        content = ''
        args = views.split(',')
        if 'all' in args:
            content += o.contentall(mode, view_id, view_name, model_name)
        else:
            content += o.xmlheader()
            if 'tree' in args:
                content += o.contentviewtree(mode, view_id, view_name, model_name)
            if 'form' in args:
                content += o.contentviewform(mode, view_id, view_name, model_name)
            if 'kanban' in args:
                content += o.contentviewkanban(mode, view_id, view_name, model_name)
            if 'filter' in args:
                content += o.contentviewfilter(mode, view_id, view_name, model_name)
            if 'action' in args:
                content += o.contentviewaction(mode, view_id, view_name, model_name)
            if 'menu' in args:
                content += o.contentenu(mode, view_id)
            content += o.xmlfooter()
        if os.path.isfile(name_view_xml):
            if sys.version_info.major < 3:
                yn = raw_input("There is a file. Do you want to overwrite it? (y/n) ")
            else:
                yn = input("There is a file. Do you want to overwrite it? (y/n) ")
            if yn == 'y':
                xml_file_w = open(name_view_xml, 'w')
                xml_file_w.write(content)
                xml_file_w.close()
        else:
            xml_file_w = open(name_view_xml, 'w')
            xml_file_w.write(content)
            xml_file_w.close()
    else:
        print ("Use the following options to create a view:\n")
        print ("\t--view new model_model_view.xml [all|form|tree|kanban|filter|menu|action]\n")
        print ("\t--view inherit model_model_view.xml [all|form|tree|kanban|filter|menu|action]\n")
    return True

def main():
    opts = sys.argv[1:]
    app = optparse.OptionParser()
    app.add_option('-a', '--app', default=False, dest='name_app', type="string", nargs=1, help="Name of app.")
    app.add_option('-o', '--object', default=False, dest='model', type="string", nargs=1, help="Name of object or model, e.g.: sale.order")
    app.add_option('-w', '--wizard', default=False, dest='wizard', type="string", nargs=1, help="Name of object or model, e.g.: sale.order")
    app.add_option('-m', '--mode', default=False, dest='mode', type='choice', choices=['new', 'inherit'], help="New or inherit option.")
    app.add_option('--views', default=False, dest='views', type='string', help="New or inherit option.")
    options, args = app.parse_args()
    if options.mode and options.model and options.views:
        createview(options.mode, options.model, options.views)
    elif options.name_app:
        createapp(options.name_app)
    elif options.model and options.mode:
        createmodel(options.model, options.mode)
    elif options.wizard and options.mode:
        createmodelwizard(options.wizard, options.mode)
    return True

if __name__ == '__main__':
    main()
