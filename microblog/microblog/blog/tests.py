from django.test import TestCase, Client

class BlogTestCase(TestCase):

    def setup(self):
        self.c = Client()

    def test_index_access(self):
        res = self.c.get('/')

        self.assertEqual(200, res.status_code)

    def test_fail_access(self):
        res = self.c.get('/unknown')
        self.assertEqual(404, res.status_code)