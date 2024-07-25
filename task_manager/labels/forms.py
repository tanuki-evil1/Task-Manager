from django import forms
from .models import Label


class LabelCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label="Имя")

    class Meta:
        model = Label
        fields = '__all__'
