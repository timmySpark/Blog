from django.contrib import admin
from app.models import *
from import_export.admin import ImportExportMixin

# Register your models here.

class BlogAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['title' ,'created_at']

admin.site.register(Blog,BlogAdmin)


class CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,CategoryAdmin)

admin.site.register(Comment)
admin.site.register(Subscribers)