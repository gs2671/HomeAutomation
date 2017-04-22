from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)
from django import forms

User=get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args, **kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")

        # user_qs=User.objects.filter(username=username)
        # user=user_qs
        # if user_qs.count()==1:
        #     user=user_qs.first()
        if username and password:
            user=authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    email= forms.EmailField(label="Email Address")
    class Meta:
        model= User
        fields = [
        'username',
        'email',
        'password',
        ]
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email had already been registered")
        return email
