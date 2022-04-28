from django.contrib import admin

from .models import Question, Availability

admin.site.register(Question)
admin.site.register(Availability)