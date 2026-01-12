from django.conf import settings
from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name         = models.CharField(unique=True)
    slug         = models.SlugField(unique=True)
    description  = models.TextField(blank=True, null=True)
    created_at   = models.DateTimeField(default=timezone.now)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'posts_categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('app.modules.posts:categories.view', kwargs={'slug': self.slug})
    

class Post(models.Model):
    title        = models.CharField(max_length=255)
    slug         = models.SlugField(unique=True)
    summary      = models.TextField()
    content      = models.TextField()
    featured     = models.BooleanField(default=False)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    author       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status       = models.CharField(max_length=30, choices=[('draft', _('Draft')), ('publish', _('Publish'))], default='draft')
    published_at = models.DateTimeField(blank=True, null=True)
    created_at   = models.DateTimeField(default=timezone.now)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table = 'posts_posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app.modules.posts:posts.view', kwargs={'pk': self.pk})
    
    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def comments(self):
        return self.comments.filter(approved=True)
    
    @property
    @admin.display(description=_('Author'))
    def author_name(self):
        return f'{self.author.first_name} {self.author.last_name}'
