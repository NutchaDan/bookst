from django.contrib import admin

from .models import Control

# class ChoiceInline(admin.TabularInline):
#     model = Choice

class ControlAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Book name',        {'fields': ['book_text']}),
        ('Date information', {'fields': ['loan_date']}),
        ('URL Image',        {'fields': ['url_image']}),
        ('User',             {'fields': ['name_user']}),
        ('Description',      {'fields': ['description']}),
    ]
    # inlines = [ChoiceInline]

admin.site.register(Control, ControlAdmin)
# admin.site.register(Choice)
