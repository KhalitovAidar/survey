from django.contrib import admin
from .models import Question, Survey
# Register your models here.
from django.contrib import admin

admin.site.register(Survey)
admin.site.register(Question)
