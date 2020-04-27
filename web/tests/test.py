from app import app
import unittest
import re


class HomeEndpointTests(unittest.TestCase):

    def setUp(self):
        '''
        Setting up response to be home-page's response
        '''
        CoronaNewsApp = app.test_client()
        self.response = CoronaNewsApp.get('/')

    def test_get(self):
        '''
        Testing response status code to see if request is successful
        '''
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        '''
        Checking if the template loaded correctly
        '''
        self.assertIn('text/html', self.response.content_type)

    def test_bootstrap_css(self):
        '''
        Making sure bootstrap loaded correctly
        '''
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)
        self.assertIn('bootstrap.min.js', response_str)

    def test_content(self):
        '''
        Testing if the template was loaded correctly
        '''
        response_str = self.response.data.decode('utf-8')
        self.assertIn(
            'Noticias mais recentes sobre o Coronavírus no Brasil', str(response_str))


class RegionEndpointTests(unittest.TestCase):

    def setUp(self):
        '''
        Setting up response to be home-page's response
        '''
        CoronaNewsApp = app.test_client()
        region = 'DF'
        self.response = CoronaNewsApp.get(f'/{region}')

    def test_content(self):
        '''
        Testing if the template was loaded accordingly to the region
        '''
        response_str = self.response.data.decode('utf-8')
        self.assertIn(
            'DF</button>', re.sub(r"[\n\t\s]*", "", str(response_str)))
