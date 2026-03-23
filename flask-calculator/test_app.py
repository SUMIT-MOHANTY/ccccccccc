import unittest
import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')

    def test_add(self):
        response = self.app.post('/api/add', json={'a': 5, 'b': 3})
        data = response.get_json()
        self.assertEqual(data['result'], 8)

if __name__ == '__main__':
    unittest.main()
