from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(OTPVerifiaction)
admin.site.register(Sheet)
admin.site.register(EmployeeData)
admin.site.register(AccountDetails)
admin.site.register(UserData)

