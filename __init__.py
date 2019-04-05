from flask import Flask
import config
from exts import db

app = Flask(__name__, static_url_path='')
app.config.from_object(config)
db.init_app(app)
with app.app_context():
    db.create_all()

from auth import auth

app.register_blueprint(auth, url_prefix='/auth')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
