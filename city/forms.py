from django import forms

class NameForm(forms.Form):
    city_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'City name'}))
