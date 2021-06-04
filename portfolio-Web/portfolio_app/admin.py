from django.contrib import admin
from . models import My_details,Project,Account
# Register your models here.
admin.site.register(My_details)
admin.site.register(Project)
admin.site.register(Account)