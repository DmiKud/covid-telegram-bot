from pony.orm import *


db = Database()


class Log(db.Entity):
    name = Required(str)
    country = Optional(str)
    date = Optional(str)
    case = Optional(str)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def add_log(name, country, date, case):
    Log(name=name, country=country, date=date, case=case)
