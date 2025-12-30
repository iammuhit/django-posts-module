from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from app.modules.posts import REDIRECT_FIELD_NAME
from app.modules.posts.forms import PostForm
from app.modules.posts.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/view.html'


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    login_url = settings.LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'posts/form.html'


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    login_url = settings.LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'posts/form.html'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('template', {
            'title': 'Update Post',
        })
        return super().get_context_data(**kwargs)


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('app.modules.posts:posts.index')
    template_name = 'posts/delete-confirmation.html'


class DraftsView(LoginRequiredMixin, generic.ListView):
    model = Post
    login_url = settings.LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'posts/drafts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True).order_by('created_at')


@login_required(login_url=settings.LOGIN_URL)
def publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()

    return redirect('app.modules.posts:posts.view', pk=pk)
