"""Heroes test case"""
import unittest

from mock import patch
from mockfirestore import MockFirestore
from main import app


class HeroesHandlerTestCase(unittest.TestCase):
    """Heroes handler"""

    def setUp(self):
        """SetUp é chamado no inicio de cada teste"""
        self.mock_db = MockFirestore()
        self.patcher = patch(
            'modules.main.MainModule.get_firestore_db', return_value=self.mock_db)
        self.patcher.start()
        self.app= app.test_client()

    def tearDown(self):
        """O tearDown é chamado no final de cada teste"""
        self.patcher.stop()
        self.mock_db.reset()

    def test_create_a_new_hero(self):
        """This test should create a new hero"""
        hero_dict = {
            'hero': {
                'name': 'Superman',
                'description': 'Superman description',
                'universe': 'dc',
                'imageUrl': 'https://super.abril.com.br/wp-content/uploads/2018/09/superman.png?w=1024'
            }
        }

        response = self.app.post(path='/heroes', json=hero_dict)

        # Conferindo se voltou 200
        self.assertEqual(response.status_code, 200)

        # Conferindo a resposta da requisição
        self.assertIsNotNone(response.get_json())
        self.assertIsNotNone(response.get_json()['id'])


if __name__ == '__main__':
    unittest.main()