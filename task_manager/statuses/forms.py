from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Status


class StatusCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label=_("Name"))

    class Meta:
        model = Status
        fields = '__all__'
