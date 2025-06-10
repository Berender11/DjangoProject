from django.contrib import admin

# Register your models here.
from .models import Feedback, Survey

admin.site.register(Feedback)
admin.site.register(Survey)