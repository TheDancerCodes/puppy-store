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


class GetSinglePuppyTest(TestCase):
    """Test module for GET single puppy API"""

    def setUp(self):
        self.moana = Puppy.objects.create(
            name='Moana', age=3, breed='Chihuahua', color='white')
        self.chinku = Puppy.objects.create(
            name='Chinku', age=5, breed='Shih Tzu', color='Brown')
        self.pendo = Puppy.objects.create(
            name='Pendo', age=4, breed='Poodle', color='Apricot')
        self.rex = Puppy.objects.create(
            name='Rex', age=4, breed='German Shepherd', color='Brown')

    def test_get_valid_single_puppy(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': self.rex.pk}))
        puppy = Puppy.objects.get(pk=self.rex.pk)
        serializer = PuppySerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_single_puppy(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
















