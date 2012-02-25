from pyramid.config import Configurator
from bankaccount.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_view('bankaccount.views.my_view',
                    context='bankaccount:resources.Root',
                    renderer='bankaccount:templates/mytemplate.pt')
    config.add_static_view('static', 'bankaccount:static', cache_max_age=3600)
    return config.make_wsgi_app()
