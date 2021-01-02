from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth import authenticate
from .models import Account, Applicant, Company


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


class RegistrationFormApplicant(ModelForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')

    class Meta:
        model = Applicant
        fields = ('first_name', 'last_name',)


class RegistrationFormCompany(ModelForm):
    name = forms.CharField(max_length=100, help_text='Name')
    field = forms.CharField(max_length=100, help_text='Field')
    about = forms.CharField(max_length=500, help_text='About')

    class Meta:
        model = Company
        fields = ('name', 'field', 'about')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


# class UserUpdateForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=100, help_text='First Name')
#     last_name = forms.CharField(max_length=100, help_text='Last Name')
#
#     class Meta:
#         model = Applicant
#         fields = [
#             'first_name',
#             'last_name',
#         ]
#
#         def save(self, commit=True):
#             account = super(UserUpdateForm, self).save(commit=False)
#             account.username = self.cleaned_data['username']
#             account.email = self.cleaned_data['email'].lower()
#             if commit:
#                 account.save()
#             return account

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)

    def save(self, commit=True):
        account = super(UserUpdateForm, self).save(commit=False)
        account.username = self.cleaned_data['username']
        account.email = self.cleaned_data['email'].lower()
        if commit:
            account.save()
        return account


class CompanyUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text='Name')
    field = forms.CharField(max_length=100, help_text='Field')
    about = forms.CharField(max_length=500, help_text='About')

    class Meta:
        model = Company
        fields = [
            'name',
            'field',
            'about',
            'link'
        ]


class ApplicantUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')

    class Meta:
        model = Applicant
        fields = [
            'first_name',
            'last_name'
        ]



