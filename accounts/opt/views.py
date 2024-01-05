from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from .helpers import send_otp_to_phone
from .models import User

from django.db import IntegrityError

@api_view(['POST'])
def send_otp(request):
    data = request.data
    if data.get('phone_number') is None:
        return Response({
            'message': 'Key phone_number is required'
        }, status=400)
    
    if data.get('password') is None:
        return Response({
            'message': 'Key password is required'
        }, status=400)

    try:
        user = User.objects.create(
            username=data.get('phone_number'),  # Assuming phone_number as username
            phone_number=data.get('phone_number'),
            otp=send_otp_to_phone(data.get('phone_number'))
        )

        user.set_password(data.get('password'))
        user.save()

        return Response({
            'message': 'OTP Sent'
        })
    except IntegrityError as e:
        return Response({
            'message': 'Error creating user: Username already exists'
        }, status=400)



@api_view(['POST'])
def verify_otp(request):
    data = request.data
    try:
        user = User.objects.get(phone_number=data.get('phone_number'))
    except User.DoesNotExist:
        return Response({
            'status': 400,
            'message': 'Invalid phone number'
        })

    if user.otp == data.get('otp'):
        # Matched OTP, you can perform additional actions here if needed
        return Response({
            'status': 200,
            'message': 'OTP matched'
        })

    return Response({
        'status': 400,
        'message': 'Invalid OTP'
    })


    


