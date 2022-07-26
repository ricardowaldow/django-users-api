from django.contrib import admin
from users.models import User

class Users(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome', 'email')
    search_fields = ('nome', 'email',)
    list_per_page = 15