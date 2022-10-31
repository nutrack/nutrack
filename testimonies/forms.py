from django import forms
from testimonies.models import Testimony

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['title', 'testimony']