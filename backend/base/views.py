from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile, CustomerProfile, SellerProfile, Service, PicsPosts, Appointment, NextAppointment
from .Serializer import (
    UserProfileSerializer, CustomerProfileSerializer, SellerProfileSerializer,
    ServiceSerializer, PicsPostsSerializer, AppointmentSerializer, NextAppointmentSerializer, UserSerializer
)

@api_view(['GET'])
def index(request):
    return Response('Hello, welcome to the API!')

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        user_data = request.data.get('user', {})
        profile_data = request.data.get('profile', {})
        
        user_serializer = UserSerializer(data=user_data)
        profile_serializer = UserProfileSerializer(data=profile_data)

        if user_serializer.is_valid() and profile_serializer.is_valid():
            user = user_serializer.save()
            profile_data['user'] = user.id  # Set user id before creating profile
            profile = profile_serializer.save()
            
            if profile.role == 'user' and profile.type == 'customer':
                customer_data = request.data.get('customer_profile', {})
                customer_data['user_profile'] = profile.id
                customer_serializer = CustomerProfileSerializer(data=customer_data)
                
                if customer_serializer.is_valid():
                    customer_serializer.save()
                else:
                    user.delete()  # Rollback user creation
                    return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
            elif profile.role == 'user' and profile.type == 'seller':
                seller_data = request.data.get('seller_profile', {})
                seller_data['user_profile'] = profile.id
                seller_serializer = SellerProfileSerializer(data=seller_data)
                
                if seller_serializer.is_valid():
                    seller_serializer.save()
                else:
                    user.delete()  # Rollback user creation
                    return Response(seller_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'User registration failed.'}, status=status.HTTP_400_BAD_REQUEST)

class CustomerProfileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = CustomerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SellerProfileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = SellerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_service(request):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PicsPostsView(APIView):
    def get(self, request):
        res=[] 
        for img in PicsPosts.objects.all(): 
            res.append({"service_type":img.service_type,
                "description":img.description,
               "image":str( img.image)
                }) 
        return Response(res) 

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = PicsPostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def add_appointment(request):
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_nextappointment(request):
    if request.method == 'POST':
        serializer = NextAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
