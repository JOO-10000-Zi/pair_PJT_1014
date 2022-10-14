from dataclasses import field
from django import forms
from .models import reviews

class ReviewsForm(forms.ModelForm):

    class Meta:
        model = reviews
        fields = "__all__"