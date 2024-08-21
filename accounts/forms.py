from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ("username",'email',  "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False

    def clean(self) -> dict[str, Any]:
        cd = self.cleaned_data
        username = cd.get('username')
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
      
        return cd
        # email =   cd.get('email')
        # if User.objects.filter(email=email).count():
        #     self.add_error('email', "email address already exists!")

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        unique_together = ('email',)
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        email = self.cleaned_data["email"]
        user.email = email
        if commit:
            user.save()
        return user
    def clean(self) -> dict[str, Any]:
        cd = self.cleaned_data
        email =   cd.get('email').lower()
        if User.objects.filter(email=email).count():
            self.add_error('email', "email address already exists!")

            
        return cd
