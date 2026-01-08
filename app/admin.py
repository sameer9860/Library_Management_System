from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'description', 'published_date')
    search_fields = ('title', 'author', 'category', 'description')
    list_filter = ('category', 'published_date')

admin.site.register(Book, BookAdmin)
