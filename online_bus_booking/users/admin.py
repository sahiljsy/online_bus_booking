from django.contrib import admin
from .models import userRecord

# Register your models here.
class userRecordAdmin(admin.ModelAdmin):
    list_display = ('username','password','email','mobileNumber','address','dateOfBirth')

admin.site.register(userRecord,userRecordAdmin)