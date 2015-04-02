from IPython.terminal.embed import embed
from sqlalchemy.exc import OperationalError

from db import engine


def database_exists():
    try:
        engine.connect()
        return True
    except OperationalError:
        print('The database "sqlalchemy_tutorial" did not exist')
        print('Please run commands below')
        print('--------------------------------------')
        print('createdb sqlalchemy_tutorial')
        print('psql sqlalchemy_tutorial < world.sql')
        print('--------------------------------------')
        return False


if database_exists():
    embed()
