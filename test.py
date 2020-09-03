try:
    from app import app
    import api
    import unittest
    import requests
except Exception as e:
    print('Some Modules are missing '.format(e))


class FlaskTestCase(unittest.TestCase):

    def test_default_route(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/abc')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_movies_failed(self):
        tester = app.test_client(self)
        response = tester.get('/movies')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_api_movies(self):
        response = api.get_films_list()
        assert isinstance(response, list)

    def test_api_people(self):
        response = api.get_people_list()
        assert isinstance(response, list)


if __name__ == '__main__':
    unittest.main()
