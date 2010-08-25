from django.contrib.admin import ModelAdmin, site
from blog.models import *

class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
site.register(Category, CategoryAdmin)

class EntryAdmin(ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter  = ('pub_date', 'categories')
    prepopulated_fields = {'slug': ('headline',)}

site.register(Entry, EntryAdmin)
