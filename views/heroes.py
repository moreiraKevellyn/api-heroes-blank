"""Heroes view"""
from flask_restful import Resource
from flask import request
from modules.hero import HeroModule


class HeroesHandler(Resource):
    """Heroes handler"""

    def get(self):
        """Get heroes"""
        try:
            pass
        except Exception as error:
            return {
                       'message': 'Error on get heroes',
                       'details': str(error)
                   }, 500

    def post(self):
        """Create a new hero"""
        try:
            if not request.is_json or 'hero' not in request.json:
                return {'message': 'Bad request'}, 400

            hero = HeroModule.create(request.json['hero'])
            return hero.to_dict()

        except Exception as error:
            return {
                       'message': 'Error on create a new hero',
                       'details': str(error)
                   }, 500
