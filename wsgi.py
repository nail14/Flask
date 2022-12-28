from werkzeug.security import generate_password_hash

from blog.app import create_app, db

app = create_app()
# app.config.from_pyfile('config.py')


# function will create all tables
@app.cli.command('init-db')
def init_db():
    db.create_all()


# add users
@app.cli.command('create-users')
def create_user():
    from blog.models import User

    db.session.add(
        User(email='nail5552@email.ru', password=generate_password_hash('test123'))
    )
    db.session.commit()
