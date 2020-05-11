from django.contrib import admin

from basic_app.models import UserProfileInfo,Exams,Question

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Exams)
admin.site.register(Question)
