"""Heroes search view"""
from flask import request
from flask_restful import Resource

from models.hero import Hero


class HeroesSearchHandler(Resource):
    """Heroes handler"""

    def get(self):
        """Get heroes"""
        try:
            heroes = Hero.search_heroes(request.args.get('name'))
            response = {
                'heroes': [],
            }
            for hero in heroes:
                response['heroes'].append(hero.to_dict())
            if response['heroes']:
                return response['heroes']
            return {'message': 'Bad request, param name is required'},400

        except Exception as error:
            return {
                       'message': 'Error on get heroes',
                       'details': str(error)
                   }, 500
