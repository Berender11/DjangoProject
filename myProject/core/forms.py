from django import forms
from .models import Feedback, Survey

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['age', 'gender', 'likes_django']
