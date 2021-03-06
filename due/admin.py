from django.contrib import admin
from .models import Due, Due_Definition


class DueAdmin(admin.ModelAdmin):
    list_display = ('id', 'due_description', 'category')
    list_display_links = ('id', 'due_description', 'category')


class DueDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_initial', 'time_end', 'day_pay', 'value', 'due')
    list_display_links = ('id', 'time_initial', 'time_end', 'day_pay', 'value', 'due')


admin.site.register(Due, DueAdmin)
admin.site.register(Due_Definition, DueDefinitionAdmin)