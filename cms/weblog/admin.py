from django.contrib import admin
from .models import Category, Entry

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title']}

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)




