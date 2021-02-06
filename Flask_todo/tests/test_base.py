from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING']=True
        app.config['WTF_CSRF_ENABLE']=False
        return app
    
    def test_app_exist(self):
        self.assertIsNone(current_app)
    
    def test_app_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    
    def test_index_redirect(self):
        response=self.client.get(url_for('index'))
        self.assertRedirects(response,url_for('hello'))
    
    def test_hello_get(self):
        response=self.client.get(url_for('hello'))
        self.assert200(response)