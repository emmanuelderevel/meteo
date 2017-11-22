from django import forms
import json

class NameForm(forms.Form):
    city_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'city name'}))

    def clean_city_name(self):
        city_name = self.cleaned_data['city_name']
        json_data = open('cities.json')
        data = json.load(json_data)
        L = []
        for i in range(0, len(data)):
            if data[i]['name'].upper() == city_name.upper():
                L = L + [data[i]]
        if len(L)==0 :
            raise forms.ValidationError("It looks like you did not enter a valid city name, please try again :)")
        return city_name

class SignUpForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'username'}))
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'email'}))
    password = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'password'}))

class ConnexionForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'password'}))
