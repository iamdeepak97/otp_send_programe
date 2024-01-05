import random
from django.conf import settings
import requests


def send_otp_to_phone(phone_number):
    try:
        otp=random.randint(1000,9999)
        # url=f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}'
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}/your_otp_template_id'
        response = requests.get(url)
        return otp
    except Exception as e:
        return None


# import requests
# import random
# from django.conf import settings  # Ensure settings import is included

# def send_otp_to_phone(phone_number):
#     try:
#         otp = random.randint(1000, 9999)
#         url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}/your_otp_template_id'
#         response = requests.get(url)
#         if response.status_code == 200:
#             return otp
#         else:
#             return None  # Failed to send OTP
#     except Exception as e:
#         return None  # Exception occurred during OTP sending
