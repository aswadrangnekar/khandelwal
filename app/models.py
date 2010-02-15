#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configuration

from google.appengine.api import memcache
from google.appengine.ext import db
from dbhelper import SerializableModel, serialize_entities, deserialize_entities

import appengine_admin

class Feedback(SerializableModel):
    full_name = db.StringProperty()
    email = db.EmailProperty()
    phone_number = db.StringProperty()
    subject = db.StringProperty()
    comment = db.TextProperty()

class Inquiry(SerializableModel):
    full_name = db.StringProperty()
    email = db.EmailProperty()
    phone_number = db.StringProperty()
    subject = db.StringProperty()
    comment = db.TextProperty()

class AdminFeedback(appengine_admin.ModelAdmin):
    model = Feedback
    listFields = ('full_name', 'email', 'phone_number', 'subject')
    editFields = ('full_name', 'email', 'phone_number', 'subject', 'comment')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by when_created desc'

class AdminInquiry(appengine_admin.ModelAdmin):
    model = Inquiry
    listFields = ('full_name', 'email', 'phone_number', 'subject')
    editFields = ('full_name', 'email', 'phone_number', 'subject', 'comment')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by when_created desc'


appengine_admin.register(AdminFeedback, AdminInquiry)
