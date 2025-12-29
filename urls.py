from django.urls import path

from app.modules.posts import views

app_name = 'app.modules.posts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='posts.index'),
    path('<int:pk>/', views.DetailView.as_view(), name='posts.view'),
    path('create/', views.CreateView.as_view(), name='posts.create'),
    path('<int:pk>/edit/', views.UpdateView.as_view(), name='posts.edit'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='posts.delete'),
    path('<int:pk>/publish/', views.publish, name='posts.publish'),
    path('drafts/', views.DraftsView.as_view(), name='posts.drafts'),
]
