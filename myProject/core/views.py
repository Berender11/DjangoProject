from django.shortcuts import render, redirect
from .forms import FeedbackForm, SurveyForm

def home_view(request):
    return render(request, 'core/home.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'core/feedback.html', {'form': form})

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SurveyForm()
    return render(request, 'core/survey.html', {'form': form})
