from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Puppy
from .serializers import PuppySerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_puppy(request, pk):
    """Function handling single elements."""
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET details of a single puppy
    if request.method == 'GET':
        serializer = PuppySerializer(puppy)
        return Response(serializer.data)
    # DELETE a single puppy
    elif request.method == 'DELETE':
        return Response({})
    # UPDATE details of a single puppy
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_puppies(request):
    """Function handling collections."""

    # get all puppies
    if request.method == 'GET':
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)
    # insert a new record for a puppy
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'age': int(request.data.get('age')),
            'breed': request.data.get('breed'),
            'color': request.data.get('color')
        }
        # Insert a new record by serializing and validating the request data
        # before inserting to the database.
        serializer = PuppySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
