from django import forms

class NameForm(forms.Form):
    city_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'City name'}))

class SignUpForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Username'}))
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Email'}))
    password = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Password'}))

class ConnexionForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Password'}))
