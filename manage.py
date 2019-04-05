from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from . import __init__

manage = Manager(__init__)
migrate = Migrate(__init__, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
