from django.contrib import admin, messages
from django.utils.translation import ngettext

from app.modules.posts.models import Category, Post

# admin.site.disable_action('delete_selected')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ['name']}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category__name', 'featured', 'status', 'published_at', 'created_at', 'updated_at')
    list_filter = ['category__name', 'author__username', 'featured']
    prepopulated_fields = {'slug': ['title']}
    search_fields = ('title', 'category__name', 'author__username')
    actions = ['make_featured', 'make_published', 'delete_selected']

    @admin.action(description='Mark as Featured')
    def make_featured(self, request, queryset):
        updated = queryset.update(featured=True)
        self.message_user(request, ngettext(
            '%d post was successfully marked as featured.',
            '%d posts were successfully marked as featured.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark as Published')
    def make_published(self, request, queryset):
        updated = queryset.update(status='publish')
        self.message_user(request, ngettext(
            '%d post was successfully marked as published.',
            '%d posts were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
