""" :mod:`flask.ext.hedwig`
    ~~~~~~~~~~~~~~~~~~~~~~~

"""
from __future__ import absolute_import
from hedwig.backends import BaseEmailBackend
from werkzeug.utils import import_string


class Hedwig(object):
    """ Flask-Hedwig Extension. """

    def __init__(self, app, template_folder='hedwig', backend=None, **kwargs):
        self.app = app
        self.template_folder = template_folder
        if backend is None:
            raise ValueError('backend must be specified')
        elif isinstance(backend, basestring):
            try:
                backend = import_string(backend)
            except ImportError:
                backend = import_string('hedwig.backends:%s' % backend)
        if not isinstance(backend, BaseEmailBackend):
            backend = backend(**backend_kwargs) 
        self.backend = backend
