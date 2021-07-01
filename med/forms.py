# from django import forms
# from django.contrib.auth.models import User
#
#
# class ContactForm(forms.ModelForm):
# 	username = forms.CharField(widget=forms.TextInput(attrs={ "id":"username","placeholder":"Username"}), max_length=30, required=True,)
# 	email = forms.CharField(widget=forms.EmailInput(attrs={ "id":"email","placeholder":"Email Address"}), max_length=100, required=True,)
# 	password = forms.CharField(widget=forms.PasswordInput(attrs={ "id":"password","placeholder":"Create Password"}))
# 	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={ "id":"retypepassword","placeholder":"Confirm Password"}), required=True, label="Confirm your password.")
#
# 	class Meta:
#
# 		model = User
# 		fields = ('username', 'email', 'password')
