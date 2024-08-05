from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Label


class LabelCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label=_("Name"))

    class Meta:
        model = Label
        fields = '__all__'
