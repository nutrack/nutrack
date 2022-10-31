from django.forms import forms
from .models import Testimony

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['title', 'testimony']