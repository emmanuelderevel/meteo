from django import forms

class NameForm(forms.Form):
    city_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'city name'}))

class SignUpForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'username'}))
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'email'}))
    password = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'password'}))

class ConnexionForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'password'}))
