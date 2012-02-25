from pyramid.httpexceptions import HTTPFound
from models import NotEnoughFunds

def my_view(request):
    return {'project':'bankaccount'}

def home(request):
    bankaccount = request.context.get_bankaccount()
    return dict(bankaccount=bankaccount)

def deposit(request):
    bankaccount = request.context.get_bankaccount()
    bankaccount.deposit(int(request.params['amount']))
    return HTTPFound(location=request.route_url('home'))

def withdraw(request):
    bankaccount = request.context.get_bankaccount()
    try:
        bankaccount.withdraw(int(request.params['amount']))
    except NotEnoughFunds:
        request.session.flash("you don't have too much money.")
    return HTTPFound(location=request.route_url('home'))

