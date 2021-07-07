from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from django.core.validators import validate_email

import json


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        try: 
            validate_email(email)
        except:
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use, choose another one '}, status=409)
        return JsonResponse({'email_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use,choose another one '}, status=409)
        return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')


    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Your password is too short.')
                    return render(request, 'authentication/register.html', context)

                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()

                messages.success(request, 'Account created successfully.')
                return render(request, 'authentication/register.html')

        return render(request, 'authentication/register.html', context)