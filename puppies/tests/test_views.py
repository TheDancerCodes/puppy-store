"""Hold all tests for our views and create a new test client for our app."""
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializer


# Initailize the APIClient app
client = Client()


class GetAllPuppiesTest(TestCase):
    """Test module for GET all puppies API"""

    def setUp(self):
        Puppy.objects.create(
            name='Moana', age=3, breed='Chihuahua', color='white')
        Puppy.objects.create(
            name='Chinku', age=5, breed='Shih Tzu', color='Brown')
        Puppy.objects.create(
            name='Pendo', age=4, breed='Poodle', color='Apricot')
        Puppy.objects.create(
            name='Rex', age=4, breed='German Shepherd', color='Brown')

    def test_get_all_puppies(self):
        # get API Response
        response = client.get(reverse('get_post_puppies'))
        # get data from DB
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
