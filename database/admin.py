from django.contrib import admin

from .models import Choice, Book

class ChoiceInline(admin.TabularInline):
    model = Choice

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Book name',        {'fields': ['book_text']}),
        ('Date information', {'fields': ['loan_date']}),
        ('URL Image',        {'fields': ['url_image']}),
        ('User',             {'fields': ['name_user']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Choice)
