import logging

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(version='1.0', title='My Demo API',
          description='A simple demonstration of a Flask RestPlus powered API')