# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Book
from .forms import UserForm
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='enter')
def main(request):
	lane='URA!!'
	
	if request.GET.get('logout'):
		logout(request)
		return redirect('/enter')
	return render(request,'lab/main.html',{'lane':lane})

def auth(request):
	errors=[]
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		password2=request.POST['password2']
		email=request.POST['email']
		first=request.POST['first_name']
		last=request.POST['last_name']
		if len(username)<5 or not username:
			errors.append('Vvedite norm login')
		if len(password)<8 or not password:
			errors.append('Vvedite norm password')
		if password != password2:
			errors.append('Paroli ne sovpadayut')
		if not email:
			errors.append('Vvedite email')
		if not first:
			errors.append('Vvedite Imya')
		if not last:
			errors.append('Vvedite Familiyu')
		if User.objects.filter(username=username).exists():
			errors.append('Takoy user exist')
		if not errors:
			user=User(username=username,email=email,first_name=first,last_name=last)
			user.save()
			user = User.objects.get(username=username)
			user.set_password(password)
			user.save()
			user = authenticate(username=username, password=password)
			if user is not None:            
				login(request, user)
				return redirect('main')
	return render(request,'lab/auth.html',{'errors':errors})

def enter(request):
	d='0'
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:            
			login(request, user)
			return redirect('main')
		else:
			d='2'
	return render(request,'lab/enter.html',{'d':d})

def auth1(request):
	if request.method == "POST":
		print (request.POST)
		form=UserForm(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			password2=request.POST['password2']
			email=request.POST['email']
			first=request.POST['first']
			last=request.POST['last']
			user=User(username=username,email=email,first_name=first,last_name=last)
			user.save()
			user = User.objects.get(username=username)
			user.set_password(password)
			user.save()
			user = authenticate(username=username, password=password)
			print (user)
			if user is not None:            
				login(request, user)
				return redirect('main')
	else:
		form=UserForm()	
	return render(request,'lab/auth1.html',{'d':form})