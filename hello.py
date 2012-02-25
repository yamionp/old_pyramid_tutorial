# -*- coding: utf-8 -*-
from datetime import date, datetime

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from paste.httpserver import serve

class MyContext(object):
    def __init__(self, request):
        self.request = request

    def get_date(self):
        return date.today()

    def greeting(self):
        now = datetime.now()
        if now.hour < 12:
            return "Good morning"
        elif now.hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"


@view_config(route_name="home", renderer="index.mak")
def index(request):
    return dict()

@view_config(route_name='hello')
def hello(request):
    return Response("hello")

if __name__ == '__main__':
    import os
    here = os.path.dirname(__file__)
    settings = {
        'mako.directories':[
            os.path.abspath(os.path.join(here, 'templates')),
            ],
        }
    config = Configurator(settings=settings,
                          root_factory=MyContext)
    config.add_route('home', '/')
    config.add_route('hello', '/hello')

    config.scan()

    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')

