from django.contrib import admin
# Register your models here.
from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display =('id', 'email', 'name', 'subject')
    list_display_link = ('id', 'subject', 'name')
    search_fields = ('email','id', 'name')
    list_per_page = 25
admin.site.register(Contact, ContactAdmin)