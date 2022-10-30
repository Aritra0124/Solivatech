from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dog, Breed
from .serializer import DogSerializer, BreedSerializer


# Create your views here.

def index(request):
    return render(request, 'index.html')


class DogList(APIView):
    def post(self, request, format=None):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        items = Dog.objects.all()
        serializer = DogSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class DogDetails(APIView):
    def get(self, request, id=None, format=None):
        if id:
            dog = Dog.objects.get(pk=id)
            serializer = DogSerializer(dog)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, id=None, format=None):
        dog = Dog.objects.get(pk=id)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, format=None):
        dog = Dog.objects.get(pk=id)
        dog.delete()
        return Response({"status": "success"}, status=status.HTTP_400_BAD_REQUEST)


class BreedList(APIView):
    def get(self, request, format=None):
        items = Breed.objects.all()
        serializer = BreedSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BreedDetails(APIView):
    def get(self, request, id=None, format= None):
        if id:
            breed = Breed.objects.get(pk=id)
            serializer = BreedSerializer(breed)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, id=None, format= None):
        breed = Breed.objects.get(pk=id)
        serializer = BreedSerializer(breed, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, format= None):
        breed = Breed.objects.get(pk=id)
        breed.delete()
        return Response({"status": "success"}, status=status.HTTP_400_BAD_REQUEST)
