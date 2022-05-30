from django.contrib import admin
from .models import *
# Register your models here.



class ResultAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    readonly_fields = ('id',)


admin.site.register(Result, ResultAdmin)
admin.site.register(Student, StudentAdmin)
