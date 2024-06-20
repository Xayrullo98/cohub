from django.contrib import admin
from myapp.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','name','client','picture1','date']


admin.site.register(Portfolio,AdminPortfolio)


class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']


admin.site.register(Category,AdminCategory)