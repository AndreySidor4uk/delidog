import peewee
from playhouse.db_url import connect
from delidog.settings import DATABASE_URL


db = connect(DATABASE_URL)


class BaseModel(peewee.Model):
    class Meta:
        database = db


class PeeweeConnectionMiddleware(object):
    def process_request(self, req, resp):
        db.connect()

    def process_response(self, req, resp, resource, req_succeeded):
        if not db.is_closed():
            db.close()
