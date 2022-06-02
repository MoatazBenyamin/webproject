import urllib

import json

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserprofileForm,ProfileUpdateForm,UserUpdateForm
from .models import Video

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        userprofileform = UserprofileForm(request.POST)

        if form.is_valid() and userprofileform.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                user = form.save()
                userprofile = userprofileform.save(commit=False)
                userprofile.user = user
                userprofile.save()
                login(request, user)
                return redirect('http://localhost:8080/log-in')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    else:
        form = SignUpForm()
        userprofileform = UserprofileForm()
    
    return render(request, 'signup.html', {'form': form, 'userprofileform': userprofileform})

@login_required
def myaccount(request):
    context = {

    }
    return render(request, 'myaccount.html')

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f'Your account have been updated successfully!')
            return redirect('http://127.0.0.1:8000/api/v1/myaccount')
    else:
        messages.success(request , f'something went wrong! pleace try again')
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile_update.html',context)

def video(request):
    video=Video.objects.all()
    return render(request,"media.html",{"video":video})