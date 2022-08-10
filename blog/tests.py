from django.test import TestCase, Client

# Create your tests here.
class TestView(TestCase):
    def test_post_list(self):
        self.assertEqual(2,2)