#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Libs to uses with otoolsdev
'''
import os

class olibdevs():
    
    def contentmanifest(self):
        content_mainfest = '''# -*- coding: utf-8 -*-
{
    'name': 'NAME OF APPS',
    'version': '',
    'category': '',
    'application': True,
    'author': 'NAME OF AUTHOR',
    'contributors': [
        'YOUR NAME <YOURUSERNAME@MAIL.COM>'
    ],
    'website': '',
    'summary': '',
    'description': """
""",
    'depends': [],
    'data': [
        #'security/ir.model.access.csv'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False
}'''
        return content_mainfest
    
    def contentinit(self):
        content_init = ''''''
        return content_init
    
    def contentsecurity(self):
        security_csv = '''id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink'''
        return security_csv
    
    def contentmodel(self, class_name, mode, model_name):
        content_model = '''# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api, _
from odoo.exceptions import Warning
from odoo.tools import float_is_zero
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import odoo.addons.decimal_precision as dp
from datetime import *
import pytz
from pytz import timezone
import logging
_logger = logging.getLogger(__name__)


class %s(models.Model):
    _%s = '%s'
    _description = ''
    
    name = fields.Char('Name')
    description = fields.Text('Description')
    
    _order = 'name'    
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The name must be unique!')
    ]
''' % (class_name, mode, model_name)
        return content_model
    
    def contentmodelwizard(self, class_name, mode, model_name):
        content_model = '''# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError
from datetime import *
import requests
import tempfile
import io
import zipfile
import os
import logging
import csv
logger = logging.getLogger(__name__)

class %s(models.TransientModel):
    _%s = '%s'
    _description = ''
    
    name = fields.Char('Name')
    description = fields.Text('Description')
    
    _order = 'name'    
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The name must be unique!')
    ]
''' % (class_name, mode, model_name)
        return content_model
    
    def contentviewtree(self, mode, view_id, view_name, model_name):
        content_h = '''
        <record id="tree_%s_1" model="ir.ui.view">
            <field name="name">tree.%s.1</field>
            <field name="model">%s</field>
            <field name="priority" eval=""/>
            <field name="inherit_id" ref=""/>
            <field name="arch" type="xml">
                <xpath expr="" position="">
                </xpath>
            </field>
        </record>
''' % (view_id, view_name, model_name)
        content_n = '''
        <record id="tree_%s" model="ir.ui.view">
            <field name="name">tree.%s</field>
            <field name="model">%s</field>
            <field name="priority" eval=""/>
            <field name="arch" type="xml">
                <tree name="" string="">
                    <field name=""/>
                </tree>
            </field>
        </record>
''' % (view_id, view_name, model_name)
        if mode == 'new':
            return content_n
        else:
            return content_h
    
    def contentviewform(self, mode, view_id, view_name, model_name):
        content_h = '''
        <record id="form_%s_1" model="ir.ui.view">
            <field name="name">form.%s.1</field>
            <field name="model">%s</field>
            <field name="priority" eval=""/>
            <field name="inherit_id" ref=""/>
            <field name="arch" type="xml">
                <xpath expr="" position="">
                </xpath>
            </field>
        </record>
''' % (view_id, view_name, model_name)
        content_n = '''
        <record id="form_%s" model="ir.ui.view">
            <field name="name">form.%s</field>
            <field name="model">%s</field>
            <field name="priority" eval=""/>
            <field name="arch" type="xml">
                <form name="" string="">
                    <header>
                    </header>
                    <sheet>
                        <field name="" widget="image" class="oe_avatar" options="{'size': [90, 90]}"/>
                        <div class="oe_title">
                            <h1>
                                <field name="name" required="1"/>
                            </h1>
                        </div>
                        <group>
                            <group>
                            </group>
                            <group>
                            </group>
                        </group>
                        <notebook>
                            <page string="">
                            </page>
                        </notebook>
                    </sheet>
                </form>
            </field>
        </record>
''' % (view_id, view_name, model_name)
        if mode == 'new':
            return content_n
        else:
            return content_h
    
    def contentviewkanban(self, mode, view_id, view_name, model_name):
        content_h = '''
        <record id="kanban_%s_1" model="ir.ui.view">
            <field name="name">kanban.%s.1</field>
            <field name="model">%s</field>
            <field name="priority" eval=""/>
            <field name="inherit_id" ref=""/>
            <field name="arch" type="xml">
                <kanban class="o_res_partner_kanban">
                    <field name=""/>
                    <templates>
                        <t t-name="kanban-box">
                            <div class="oe_kanban_global_click o_res_partner_kanban">
                                <div class="oe_kanban_details">
                                </div>
                            </div>
                        </t>
                    </templates>
                </kanban>
            </field>
        </record>
''' % (view_id, view_name, model_name)
        content_n = '''
        <record id="kanban_%s" model="ir.ui.view">
            <field name="name">kanban.%s</field>
            <field name="model">%s</field>
            <field name="priority" eval=""/>
            <field name="arch" type="xml">
                <kanban class="o_res_partner_kanban">
                    <field name=""/>
                    <templates>
                        <t t-name="kanban-box">
                            <div class="oe_kanban_global_click o_res_partner_kanban">
                                <div class="oe_kanban_details">
                                </div>
                            </div>
                        </t>
                    </templates>
                </kanban>
            </field>
        </record>
''' % (view_id, view_name, model_name)
        if mode == 'new':
            return content_n
        else:
            return content_h
    
    def contentviewaction(self, mode, view_id, view_name, model_name):
        content = '''
        <record id="action_%s" model="ir.actions.act_window">
            <field name="name">%s</field>
            <field name="type">ir.actions.act_window</field>
            <field name="res_model">%s</field>
            <field name="view_type">form</field>
            <field name="view_mode">tree,form</field>
            <field name="domain">[]</field>
            <field name="context">{"search_default_":1,'default_':1}</field>
            <field name="search_view_id" ref="filter_%s"/>
            <field name="help" type="html">
                <p class="o_view_nocontent_smiling_face">
                    Click to add a new record.
                </p>
            </field>
        </record>
''' % (view_id, view_name, model_name, view_id)
        return content
    
    def contentviewfilter(self, mode, view_id, view_name, model_name):
        content_h = '''
        <record id="filter_%s_1" model="ir.ui.view">
            <field name="name">filter.%s.1</field>
            <field name="model">%s</field>
            <field name="priority" eval=""/>
            <field name="inherit_id" ref=""/>
            <field name="arch" type="xml">
                <xpath expr="" position="">
                </xpath>
            </field>
        </record>
''' % (view_id, view_name, model_name)
        content_n = '''
        <record id="filter_%s" model="ir.ui.view">
            <field name="name">filter.%s</field>
            <field name="model">%s</field>
            <field name="priority" eval=""/>
            <field name="arch" type="xml">
                <search string="">
                    <field name="name" filter_domain="['|','|',('name','ilike',self),('description','ilike',self)]"/>
                    <filter name="" help="" domain="[('user_id','=',uid)]"/>
                    <separator/>
                    <filter string="" name="" domain="[]"/>
                    <group expand="0" name="group_by" string="">
                        <filter name="" string="" context="{}"/>
                    </group>
                </search>
            </field>
        </record>
''' % (view_id, view_name, model_name)
        if mode == 'new':
            return content_n
        else:
            return content_h
    
    def contentmenu(self, mode, view_id):
        content = '''
        <menuitem id="menu_%s"
            name=""
            parent=""
            action="action_%s"
            sequence=""
            groups=""
        />
''' % (view_id, view_id)
        return content
    
    
    def xmlheader(self):
        content = '''<?xml version="1.0"?>
<odoo>
    <data>
'''
        return content
    
    def xmlfooter(self):
        content = '''
    </data>
</odoo>
'''
        return content
    
    def contentall(self, mode, view_id, view_name, model_name):
        content = ''
        content += self.xmlheader()
        content += self.contentviewtree(mode, view_id, view_name, model_name)
        content += self.contentviewform(mode, view_id, view_name, model_name)
        content += self.contentviewkanban(mode, view_id, view_name, model_name)
        content += self.contentviewfilter(mode, view_id, view_name, model_name)
        content += self.contentviewaction(mode, view_id, view_name, model_name)
        content += self.contentmenu(mode, view_id)
        content += self.xmlfooter()
        return content
    
    def otreebuilder(self, name_mod):
        dic_tree = {
            'main_dirs': ['data', 'i18n', 'models', 'security', 'static', 'views', 'wizard', 'report', 'test'],
            'sub_dirs': ['static/description', 'static/img', 'static/src', 'static/src/css', 'static/src/less', 'static/src/js']
        }
        if not os.path.exists(name_mod):
            os.mkdir(name_mod)
            for md in dic_tree['main_dirs']:
                mdir = os.path.join(name_mod, md)
                os.mkdir(mdir)
            for sd in dic_tree['sub_dirs']:
                sdir = os.path.join(name_mod, sd)
                os.mkdir(sdir)
        else:
            print ("This apps exists.")
            return False
        return True
    
    def ofilesbuilder(self, name_mod):
        
        manifest = '__manifest__.py'
        manifest_r = os.path.join(name_mod, manifest)
        if not os.path.isfile(manifest_r):
            content = self.contentmanifest()
            manifest_w = open(manifest_r, 'w')
            manifest_w.write(content)
            manifest_w.close()
        
        security = 'security/ir.model.access.csv'
        security_r = os.path.join(name_mod, security)
        if not os.path.isfile(security_r):
            content = self.contentsecurity()
            security_w = open(security_r, 'w')
            security_w.write(content)
            security_w.close()
        
        inits = [ '%s' % name_mod, '%s/models' % name_mod, '%s/wizard' % name_mod, '%s/test' % name_mod]
        init = '__init__.py'
        for i in inits:
            init_r = os.path.join(i, init)
            if not os.path.isfile(init_r):
                content = self.contentinit()
                init_w = open(init_r, 'w')
                init_w.write(content)
                init_w.close()
        
        return True


