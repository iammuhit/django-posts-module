from django.urls import path

from . import views

app_name = 'app.modules.posts'

urlpatterns = [
    path('', views.index, name='posts.index'),
]
