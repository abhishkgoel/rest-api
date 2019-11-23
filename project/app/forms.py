from django import forms
from .models import Para

class AppForm(forms.ModelForm):
    class Meta:
        model = Para
        fields = '__all__'