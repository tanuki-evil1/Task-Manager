from django import forms
from .models import Status


class StatusCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label="Имя")

    class Meta:
        model = Status
        fields = '__all__'
