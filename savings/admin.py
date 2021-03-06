from django.contrib import admin
from .models import Bank, Saved_Money, Receive


class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    list_display_links = ('id', 'description')


class SavingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'bank')
    list_display_links = ('id', 'value', 'bank')


class ReceiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_initial', 'time_end', 'description', 'value')
    list_display_links = ('id', 'time_initial', 'time_end', 'description', 'value')


admin.site.register(Saved_Money, SavingsAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Receive, ReceiveAdmin)