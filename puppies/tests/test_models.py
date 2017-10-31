from django.test import TestCase
from ..models import Puppy


class PuppyTest(TestCase):
    """Test module for Puppy model."""

    def setUp(self):
        Puppy.objects.create(
            name='Moana', age=3, breed='Chihuahua', color='white')
        Puppy.objects.create(
            name='Chinku', age=5, breed='Shih Tzu', color='Brown')

    def test_puppy_breed(self):
        puppy_moana = Puppy.objects.get(name='Moana')
        puppy_chinku = Puppy.objects.get(name='Chinku')
        self.assertEqual(
            puppy_moana.get_breed(), "Moana belongs to Chihuahua breed.")
        self.assertEqual(
            puppy_chinku.get_breed(), "Chinku belongs to Shih Tzu breed.")
