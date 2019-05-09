from flask_restplus import fields
from restplus import api

user_post = api.model('user post', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user post'),
    'username': fields.String(required=True, description='username'),
    'email': fields.String(required=True, description='email'),
})

blog_post = api.model('blog post', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'blog_name': fields.String(required=True, description='blog_name'),
    'blog_content': fields.String(required=True, description='blog_content'),
    'create_time': fields.Date(required=True, description='create_time'),
})

