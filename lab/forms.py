# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
	username=forms.CharField(label="Логин", max_length=30, required=True)
	password=forms.CharField(label="Пароль", required=True)
	password2=forms.CharField(label="Пароль еще раз", required=True)
	email=forms.CharField(label="email", required=True)
	first=forms.CharField(label="Имя", required=True)
	last=forms.CharField(label="Фамилия", required=True)

	def clean(self):
		cleaned_data = super(UserForm, self).clean()
		pas = cleaned_data.get("password")
		pas2 = cleaned_data.get("password2")
		login=cleaned_data.get("username")
		if len(pas) < 8:
			raise forms.ValidationError(
				"Пароль короткий"
			)
		if len(login) < 5:
			raise forms.ValidationError(
				"Login короткий"
			)
		if pas != pas2:
            # Only do something if both fields are valid so far.
			
			raise forms.ValidationError(
				"Пароли не совпадают"
			)
		if User.objects.filter(username=login).exists():
			raise forms.ValidationError(
				"Пользователь существует"
			)
