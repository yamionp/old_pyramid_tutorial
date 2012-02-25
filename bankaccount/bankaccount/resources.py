
from sqlalchemy.orm.exc import NoResultFound
from models import DBSession, BankAccount

class Root(object):
    def __init__(self, request):
        self.request = request

    def get_bankaccount(self):
        try:
            return DBSession.query(BankAccount).filter_by(name=u'default').one()
        except NoResultFound:
            return None




