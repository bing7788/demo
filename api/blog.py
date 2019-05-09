from flask import request
from flask_restplus import Resource
from handler import create_user, update_user, delete_user
from serializers import blog_post
from parsers import pagination_arguments
from databasemodel.user import User
from restplus import api

ns = api.namespace('blogs', description ='blogs')


@ns.route('/')
class BlogCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(blog_post)
    def get(self):
        """
        Returns list of user posts.
        """
        user_query = User.query.all()
        print("1", type(user_query))

        return user_query

    @api.expect(blog_post)
    def post(self):
        """
        Create a new user
        """
        print(request.json)
        create_user(request.json)
        return None, 201