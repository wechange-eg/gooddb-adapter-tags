from django.contrib import admin

from .models import Tag, Category

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category', )

admin.site.register(Tag, TagAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

