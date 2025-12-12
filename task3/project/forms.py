from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "developers"]

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        if not description:
            raise forms.ValidationError("description is empty!!!")

        return description
