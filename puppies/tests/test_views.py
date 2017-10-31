"""Hold all tests for our views and create a new test client for our app."""
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializer


# Initailize the APIClient app
client = Client()
