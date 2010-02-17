#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configuration

from google.appengine.api import memcache
from google.appengine.ext import db
from dbhelper import MAX_COUNT, CACHE_DURATION, SerializableModel, serialize_entities, deserialize_entities
from utils import slugify as u_slugify
from aetycoon import TransformProperty
import appengine_admin
import markup

def slugify(s):
    return u_slugify(s.lower())

render_markup = markup.render_markdown

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

class Project(SerializableModel):
    title = db.StringProperty()
    location = db.StringProperty()
    subtitle = db.StringProperty()
    description = db.TextProperty()
    cover_thumb_url = db.URLProperty()
    cover_picture_url = db.URLProperty()
    description_html = db.TextProperty()
    slug = TransformProperty(title, slugify)
    
    development_status = db.StringProperty(choices=('ongoing', 'complete'))

    @classmethod
    def get_by_slug(cls, slug):
        cache_key = 'Project.get_by_slug(%s)' % slug
        entity = deserialize_entities(memcache.get(cache_key))
        if not entity:
            entity = Project.all().filter('slug = ', slug).get()
            memcache.set(cache_key, serialize_entities(entity), CACHE_DURATION)
        return entity

    @classmethod
    def get_all_complete(cls):
        cache_key = 'Project.get_all_complete()'
        entities = deserialize_entities(memcache.get(cache_key))
        if not entities:
            entities = Project.all() \
                .filter('development_status = ', 'complete') \
                .order('title') \
                .fetch(MAX_COUNT)
            memcache.set(cache_key, serialize_entities(entities), CACHE_DURATION)
        return entities

    @classmethod
    def get_all_ongoing(cls):
        cache_key = 'Project.get_all_ongoing()'
        entities = deserialize_entities(memcache.get(cache_key))
        if not entities:
            entities = Project.all() \
                .filter('development_status = ', 'ongoing') \
                .order('title') \
                .fetch(MAX_COUNT)
            memcache.set(cache_key, serialize_entities(entities), CACHE_DURATION)
        return entities


    def put(self):
        self.description_html = render_markup(self.description)
        super(Project,self).put()

class ProjectFloorPlan(SerializableModel):
    caption = db.StringProperty()
    thumb_url = db.URLProperty()
    picture_url = db.URLProperty()
    project = db.ReferenceProperty(Project, collection_name='floor_plans')

class ProjectPhoto(SerializableModel):
    caption = db.StringProperty()
    thumb_url = db.URLProperty()
    picture_url = db.URLProperty()
    project = db.ReferenceProperty(Project, collection_name='photos')

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

class AdminProject(appengine_admin.ModelAdmin):
    model = Project
    listFields = ('title', 'subtitle', 'slug', 'location', 'development_status',)
    editFields = ('title', 'subtitle', 'location', 'development_status', 'cover_thumb_url', 'cover_picture_url', 'description')
    readonlyFields = ('slug', 'description_html', 'when_modified', 'when_created')
    listGql = 'order by title asc'
    
class AdminProjectPhoto(appengine_admin.ModelAdmin):
    model = ProjectPhoto
    listFields = ('caption', 'thumb_url', 'picture_url')
    editFields = ('caption', 'thumb_url', 'picture_url')
    listGql = 'order by caption asc'

class AdminProjectFloorPlan(appengine_admin.ModelAdmin):
    model = ProjectFloorPlan
    listFields = ('caption', 'thumb_url', 'picture_url',)
    editFields = ('caption', 'thumb_url', 'picture_url',)
    listGql = 'order by caption asc'
    
appengine_admin.register(AdminFeedback,
    AdminInquiry,
    AdminProject,
    AdminProjectFloorPlan,
    AdminProjectPhoto)
