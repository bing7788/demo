from flask_restplus import fields
from restplus import api

user_post = api.model('user post', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user post'),
    'username': fields.String(required=True, description='username'),
    'email': fields.String(required=True, description='email'),
})

