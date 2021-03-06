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


class CreateNewPuppyTest(TestCase):
    """Test module for inserting a new puppy"""

    def setUp(self):
        self.valid_payload = {
            'name': 'Moana',
            'age': 3,
            'breed': 'Chihuahua',
            'color': 'White'
        }

        self.invalid_payload = {
            'name': '',
            'age': 3,
            'breed': 'Chihuahua',
            'color': 'White'
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePuppyTest(TestCase):
    """ Test module for updating an existing puppy record """

    def setUp(self):
        self.moana = Puppy.objects.create(
            name='Moana', age=3, breed='Chihuahua', color='white')
        self.chinku = Puppy.objects.create(
            name='Chinku', age=5, breed='Shih Tzu', color='Brown')

        self.valid_payload = {
            'name': 'Mukhana',
            'age': 4,
            'breed': 'Great Dane',
            'color': 'Apricot'
        }

        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Great Dane',
            'color': 'Apricot'
        }

    def test_valid_update_puppy(self):
        response = client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.moana.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_puppy(self):
        response = client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.moana.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePuppyTest(TestCase):
    """ Test module for deleting an existing puppy record """

    def setUp(self):
        self.moana = Puppy.objects.create(
            name='Moana', age='3', breed='Chihuahua', color='white')
        self.chinku = Puppy.objects.create(
            name='Chinku', age=5, breed='Shih Tzu', color='Brown')

    def test_valid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_puppy', kwargs={'pk': self.moana.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
