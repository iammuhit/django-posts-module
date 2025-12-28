from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author       = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title        = models.CharField(max_length=200)
    content      = models.TextField()
    published_at = models.DateTimeField(blank=True, null=True)
    created_at   = models.DateTimeField(default=timezone.now)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts.view', kwargs={'pk': self.pk})
    
    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def comments(self):
        return self.comments.filter(approved=True)
