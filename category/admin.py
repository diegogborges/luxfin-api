from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    list_display_links = ('id', 'description')


admin.site.register(Category, CategoryAdmin)