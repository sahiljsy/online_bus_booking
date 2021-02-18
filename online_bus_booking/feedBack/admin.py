from django.contrib import admin
from .models import FeedBack
# Register your models here.


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('id','email','ratings','suggestions')


admin.site.register(FeedBack,FeedBackAdmin)