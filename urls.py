from django.urls import path

from app.modules.posts import views

app_name = 'app.modules.posts'

urlpatterns = [
    path('', views.posts.IndexView.as_view(), name='posts.index'),
    path('create/', views.posts.CreateView.as_view(), name='posts.create'),
    path('<int:pk>/', views.posts.DetailView.as_view(), name='posts.view'),
    path('<int:pk>/edit/', views.posts.UpdateView.as_view(), name='posts.edit'),
    path('<int:pk>/delete/', views.posts.DeleteView.as_view(), name='posts.delete'),
    path('<int:pk>/publish/', views.posts.publish, name='posts.publish'),
    path('drafts/', views.posts.DraftsView.as_view(), name='posts.drafts'),
]
