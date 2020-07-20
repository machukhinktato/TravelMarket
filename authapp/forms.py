from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
import random
import hashlib

from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ' '


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ['username', 'first_name',
                  'password1', 'password2',
                  'email', 'age', 'avatar']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ' '

        def clean_age(self):
            data = self.cleaned_data['age']
            if data < 18:
                raise forms.ValidationErrors(
                    'Забронировать размещение возможно лишь с 18-ти лет')

            return data

        def save(self):
            user = super(ShopUserRegisterForm, self).save()
            user.is_active = False
            salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
            user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
            user.save()

            return user

class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = [
            'username', 'first_name', 'email', 'age', 'avatar', 'password'
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(self, *args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ' '
                if field_name == 'password':
                    field.widget = forms.HiddenInput()

        def clean_age(self):
            data = self.cleaned_data['age']
            if data < 18:
                raise forms.ValidationErrors(
                    'Забронировать размещение возможно лишь с 18-ти лет')

            return data