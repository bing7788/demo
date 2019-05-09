from flask import request
from flask_restplus import Resource
from handler import create_user, update_user, delete_user
from serializers import user_post
from parsers import pagination_arguments
from databasemodel.user import User
from restplus import api


ns = api.namespace('users', description='Operations related to blog posts')


@ns.route('/')
class UserCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(user_post)
    def get(self):
        """
        Returns list of user posts.
        """
        user_query = User.query.all()
        print("1", type(user_query))

        return user_query

    @api.expect(user_post)
    def post(self):
        """
        Create a new user
        """
        print(request.json)
        create_user(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'user not found')
class UserItem(Resource):

    @api.expect(user_post)
    @api.response(204, 'user successfully updated.')
    def put(self, id):
        """
        Update a user post
        """
        print("id: ", id)
        data = request.json
        print("data: ", data)
        update_user(id, data)
        return None, 204

    @api.response(204, 'user successfully deleted')
    def delete(self, id):
        """
        Delete user
        """
        delete_user(id)
        return None, 204

