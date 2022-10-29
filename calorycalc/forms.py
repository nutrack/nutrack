from django import forms
from calorycalc.models import caloryInfo

class TaskForm(forms.ModelForm):
    class Meta:
        model = caloryInfo
        fields=['calory']