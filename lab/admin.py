from django.contrib import admin
from .models import Book



class PostAdmin(admin.ModelAdmin):
	list_display = ('name','id')
	list_filter = ('name', 'author')
	search_fields = ['name']


# Register your models here.
admin.site.register(Book, PostAdmin)