#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Main handlers.
# Copyright (c) 2010 happychickoo.
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import configuration

import logging
import utils
import tornado.web
import tornado.wsgi

from google.appengine.api import memcache
from google.appengine.ext import db, webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from utils import BaseRequestHandler

# Set up logging.
logging.basicConfig(level=logging.DEBUG)

class IndexHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render('index.html')

class ContactHandler(BaseRequestHandler):
    def get(self):
        self.render('contact.html')

    def post(self):
        full_name = self.get_argument('full_name')
        email = self.get_argument('email')
        phone_number = self.get_argument('phone_number')
        subject = self.get_argument('subject')
        comment = self.get_argument('comment')
        
        from models import Feedback
        feedback = Feedback()
        feedback.full_name = full_name
        feedback.email = email
        feedback.phone_number = phone_number
        feedback.subject = subject
        feedback.comment = comment
        feedback.put()
        
        self.redirect("/")

class InquiryHandler(BaseRequestHandler):
    def get(self):
        self.render('inquiry.html')

    def post(self):
        full_name = self.get_argument('full_name')
        email = self.get_argument('email')
        phone_number = self.get_argument('phone_number')
        subject = self.get_argument('subject')
        comment = self.get_argument('comment')

        from models import Inquiry
        inquiry = Inquiry()
        inquiry.full_name = full_name
        inquiry.email = email
        inquiry.phone_number = phone_number
        inquiry.subject = subject
        inquiry.comment = comment
        inquiry.put()

        self.redirect("/")

class ProjectsHandler(BaseRequestHandler):
    def get(self):
        from models import Project
        completed_projects = Project.get_all_complete()
        ongoing_projects = Project.get_all_ongoing()
        self.render('projects.html', 
            completed_projects=completed_projects,
            ongoing_projects=ongoing_projects)

class ProjectInformationHandler(BaseRequestHandler):
    def get(self, id_or_slug):
        from models import Project
        try:
            id = int(id_or_slug, 10)
            project = Project.get_by_id(id)
        except ValueError:
            project = Project.get_by_slug(id_or_slug)
        self.render('project_information.html', project=project)

class AboutHandler(BaseRequestHandler):
    def get(self):
        self.render('about.html')

settings = {
    "debug": configuration.DEBUG,
    #"xsrf_cookies": True,
    "template_path": configuration.TEMPLATE_PATH,
}
urls = (
    (r'/', IndexHandler),
    (r'/about/?', AboutHandler),
    (r'/contact/?', ContactHandler),
    (r'/inquiry/?', InquiryHandler),
    (r'/projects/?', ProjectsHandler),
    (r'/project/(.*)/?', ProjectInformationHandler),
)
application = tornado.wsgi.WSGIApplication(urls, **settings)

def main():
    from gaefy.db.datastore_cache import DatastoreCachingShim
    DatastoreCachingShim.Install()
    run_wsgi_app(application)
    DatastoreCachingShim.Uninstall()

if __name__ == '__main__':
    main()
