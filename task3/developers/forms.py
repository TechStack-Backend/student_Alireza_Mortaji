from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import Developer, Skill


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ["first_name", "last_name", "age", "email"]


Skill_formset = inlineformset_factory(Developer, Skill, fields=["title", "description"], extra=1, can_delete=True, widgets={
    'name': forms.TextInput(attrs={'class': 'form-control'}),
    'level': forms.Select(attrs={'class': 'form-control'}),
})
