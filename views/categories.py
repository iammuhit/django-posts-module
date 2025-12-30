from django.conf import settings
from django.utils import timezone
from django.views import generic

from app.modules.posts.models import Category


class IndexView(generic.ListView):
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return Category.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')


class SingleView(generic.DetailView):
    model = Category
    template_name = 'categories/single.html'
