from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stadup




class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user_name', 'done', 'todo', 'problems', 'publication')
    list_display_links = ('id', 'user_name', 'done', 'todo', 'problems', 'publication')
    list_filter = ['publication', ]
    search_fields = ['user_name', ]


admin.site.register(Stadup, AuthorAdmin)
