from django import forms
#from django.contrib.auth import(
#     authenticate,
#     get_user_model,
#     login,
#     logout,
# )
from ProductList.models import *

class CommentForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Type your Comment'}), label='',required = False)

#User=get_user_model()

class CustomUserLoginForm(forms.Form):
    username = forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args, **kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")

        # user_qs=User.objects.filter(username=username)
        # user=user_qs
        # if user_qs.count()==1:
        #     user=user_qs.first()
        #if username and password:
        #    user=authenticate(username=username, password=password)
        #    if not user:
        #        raise forms.ValidationError("This user does not exist")

        #    if not user.check_password(password):
        #        raise forms.ValidationError("Incorrect password")

        #    if not user.is_active:
        #        raise forms.ValidationError("This user is not active")
        return super(CustomUserLoginForm, self).clean(*args, **kwargs)

class CustomUserRegistrationForm(forms.ModelForm):
    username=forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)
    email= forms.EmailField(label="Email Address")
# First option is data value sshould be changed to item code later
    OPTIONS = [
            ("AmazonEcho", "AmazonEcho"),
            ("Google Home", "Google Home"),
            ("Ring Video Doorbell","Ring Video Doorbell"),
            ('Logitech Harmony Home Hub','Logitech Harmony Home Hub'),
            ('Nest Thermostat','Nest Thermostat'),
            ('Ecobee Remote Sensor','Ecobee Remote Sensor'),
            ('Philips Hue','Philips Hue'),
            ('Bose sound link Bluetooth Speaker','Bose sound link Bluetooth Speaker')
            ]
    devices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS)
    class Meta:
        model= CustomUser
        fields = [
        'username',
        'email',
        'password',
        'devices'
        ]

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_qs=CustomUser.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email had already been registered")
        return email
