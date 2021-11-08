from django.test import TestCase

# Create your tests here.

# python manage.py test
from vins.models import Vin


class VinModelTest(TestCase):
    def setUp(self):
        Vin.objects.create(title='just a test')
    
    def test_title_content(self):
        vin=Vin.objects.get(id=1)
        expected_object_name = f'{vin.title}'
        self.assertEqual(expected_object_name, 'just a test')