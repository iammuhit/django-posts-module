from django.contrib import admin

from app.modules.posts.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)
