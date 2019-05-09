from databasemodel.user import User
from databasemodel import db


def create_user(data):
    username = data.get('username')
    email = data.get('email')
    user = User(username, email)
    db.session.add(user)
    db.session.commit()


def update_user(user_id, data):
    user = User.query.filter(User.id == user_id).one()
    print("type of user:", type(user))
    print("user.username:", user.username)
    user.username = data.get('username')
    user.email = data.get('email')
    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    user = User.query.filter(User.id == user_id).one()
    db.session.delete(user)
    db.session.commit()
