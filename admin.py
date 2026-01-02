from django.contrib import admin

from app.modules.posts.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'created_at', 'updated_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category__name', 'featured', 'status', 'published_at', 'created_at', 'updated_at')
    search_fields = ('title', 'category__name', 'author__username')
