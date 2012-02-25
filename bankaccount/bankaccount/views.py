from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from models import NotEnoughFunds

def my_view(request):
    return {'project':'bankaccount'}

@view_config(route_name='home', renderer="index.mak")
def home(request):
    bankaccount = request.context.get_bankaccount()
    return dict(bankaccount=bankaccount)

@view_config(route_name='deposit')
def deposit(request):
    bankaccount = request.context.get_bankaccount()
    bankaccount.deposit(int(request.params['amount']))
    return HTTPFound(location=request.route_url('home'))

@view_config(route_name='withdraw')
def withdraw(request):
    bankaccount = request.context.get_bankaccount()
    try:
        bankaccount.withdraw(int(request.params['amount']))
    except NotEnoughFunds:
        request.session.flash("you don't have too much money.")
    return HTTPFound(location=request.route_url('home'))

