from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from . import models,forms

def BasicView(request):
    return render(request,'basic.html')

def SignupView(request):
    help_text = "enter a phone number like 9---------"
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user.save()
            user = authenticate(username = user.username, password = raw_password ,email = 'email')
            request.session.set_expiry(0)
            request.session['username'] = request.user.username
            request.session.save()
            request.session.set_test_cookie()
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            else:
                print("Please enable cookies and try again.")
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            password = ''
            for i in raw_password :
                position = alphabet.find(i)
                newposition = (position + 5) % 62
                password += alphabet[newposition]
            date = datetime.now()
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            password1 = ''
            for i in password:
                pos = alphabet.find(i)
                newpos = (pos - 5) % 62
                password1 += alphabet[newpos]
            db = models.Information.objects.create(username = user.username, password = password1,date = date,email = email)
            db.save()
            subject = 'Signed up'
            message = 'hello! welcom to our site. your sign up was successful'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail( subject, message, email_from, recipient_list )
            login(request, user)
            return redirect('/profile')
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form,'help_text' : help_text})

def LoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        for l in models.Information.objects.all():
            if str(l.username) == username :
                if l.password == password :
                    request.session.set_expiry(0)
                    request.session['username'] = request.user.username
                    request.session.save()
                    request.session.set_test_cookie()
                    if request.session.test_cookie_worked():
                        request.session.delete_test_cookie()
                    else:
                        print("Please enable cookies and try again.")
                    login(request, user)
                    return redirect('/profile')
        return render(request, 'login.html', {'error': 'Username or Password is incorrect.'})
    else:
        return render(request,'login.html')

def ProfileView(request):
    if not request.user.is_active :
        return HttpResponse("<h1>sorry!you should be log in !</h1>")
    if request.user.is_active :
        context = {}
        for l in models.Information.objects.all():
            username1 = str(l.username)
            username2 = str(request.user.username)
            if username1 == username2:
                if l.profile == "" :
                    context['url'] = 'url'
                    break
                else :
                    context['profile'] = l.profile
                    break
        context['username'] = request.user.username
        email = ""
        for l in models.Information.objects.all():
            username1 = str(l.username)
            username2 = str(request.user.username)
            if username1 == username2:
                email = l.email
                break
        context['email'] = email
        return render(request,'profile.html',context)

def UploadـProfileView(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
        models.Information.objects.filter(username = request.user.username).update(profile = fs.url(name))
    return render(request,'upload.html',context)

def UserView(request):
        list = []
        for l in models.Information.objects.all():
            list.append(l.username)
            list.append(l.password)
            list.append(l.email)
            list.append(l.date)
            profile = str(l.profile)
            list.append(profile)
        return JsonResponse(list ,safe = False)

def LogoutView(request):
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    return render(request,'logout.html')

def Change_passwordView(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            raw_password = form.cleaned_data.get('new_password1')
            oldpassword = form.cleaned_data.get('old_password')
            for l in models.Information.objects.all():
                if str(l.username) == str(request.user) :
                    if l.password == oldpassword :
                        models.Information.objects.filter(username = l.username).update(password = raw_password)
            return redirect('/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

def Check_emailView(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        for l in models.Information.objects.all():
            if str(l.username) == str(username) :
                if l.email == email :
                    userid = l.id
                    subject = 'ًReset Password'
                    message = 'hello!\nyou want to reset your password!\nplease click on the link\nhttp://127.0.0.1:8000/'+ str(userid) +'/resetـpasssword/'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email, ]
                    send_mail(subject, message, email_from, recipient_list)
                    return  render(request,'confirm_email.html')
        return render(request, 'password_reset_email.html',{'error' : 'username or email is incorrect'})
    return  render(request,'password_reset_email.html')

def Reset_passwordView(request,username_id):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        form = forms.ResetPasswordForm(request.POST)
        if form.is_valid() :
            if password1 == password2 :
                for l in models.Information.objects.all():
                    if str(username_id) == str(l.id) :
                        models.Information.objects.filter(username = l.username).update(password = password1)
                        user = User.objects.get(username = l.username)
                        user.set_password(password1)
                        user.save()
                        return redirect('/login')
                return redirect('/check_email')
            return render(request, 'reset_password.html',{'error' : 'The two passwords entered do not match'})
        else :
            return render(request, 'reset_password.html', {'error': 'The password entered is incorrect'})
    return render(request,'reset_password.html')
