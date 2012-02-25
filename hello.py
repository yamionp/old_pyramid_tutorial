# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from paste.httpserver import serve

@view_config(route_name='home')
def index(request):
    return Response("home")

@view_config(route_name='hello')
def hello(request):
    return Response("hello")

if __name__ == '__main__':
    config = Configurator()
    config.add_route('home', '/')
    config.add_route('hello', '/hello')

    config.scan()

    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')