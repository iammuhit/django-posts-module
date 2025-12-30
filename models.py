from django.conf import settings
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

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('app.modules.posts:categories.view', kwargs={'slug': self.slug})
    


class Post(models.Model):
    author       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title        = models.CharField(max_length=200)
    content      = models.TextField()
    published_at = models.DateTimeField(blank=True, null=True)
    created_at   = models.DateTimeField(default=timezone.now)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app.modules.posts:posts.view', kwargs={'pk': self.pk})
    
    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def comments(self):
        return self.comments.filter(approved=True)
