""" :mod:`flask.ext.hedwig`
    ~~~~~~~~~~~~~~~~~~~~~~~

"""
from __future__ import absolute_import
from hedwig.backends.base import BaseEmailBackend
from werkzeug.utils import import_string


class Hedwig(object):
    """ Flask-Hedwig Extension. """

    def __init__(self, app, template_folder, backend, **backend_kwargs):
        self.app = app
        self.template_folder = template_folder
        if isinstance(backend, basestring):
            backend = import_string(backend)
        if not isinstance(backend, BaseEmailBackend):
            backend = backend(**backend_kwargs) 
        self.backend = backend
