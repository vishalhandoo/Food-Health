# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    height = forms.FloatField(label='Height (in meters)')
    weight = forms.FloatField(label='Weight (in kg)')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'height', 'weight')

    def clean_height(self):
        height = self.cleaned_data['height']
        if height <= 0:
            raise forms.ValidationError("Height must be a positive number.")
        return height

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight <= 0:
            raise forms.ValidationError("Weight must be a positive number.")
        return weight
