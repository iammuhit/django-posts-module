from app.modules.posts.models import Category


def categories(request):
    return { 'categories': Category.objects.all() }
