from django.contrib import admin

from .models import Tag, Category

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

