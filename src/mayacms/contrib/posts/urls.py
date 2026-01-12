from django.urls import path

from mayacms.contrib.posts import views

app_name = 'mayacms.contrib.posts'

urlpatterns = [
    path('categories/', views.categories.IndexView.as_view(), name='categories.index'),
    path('categories/<slug:slug>/', views.categories.SingleView.as_view(), name='categories.view'),

    path('', views.posts.IndexView.as_view(), name='posts.index'),
    path('create/', views.posts.CreateView.as_view(), name='posts.create'),
    path('<int:pk>/', views.posts.SingleView.as_view(), name='posts.view'),
    path('<int:pk>/edit/', views.posts.UpdateView.as_view(), name='posts.edit'),
    path('<int:pk>/delete/', views.posts.DeleteView.as_view(), name='posts.delete'),
    path('<int:pk>/publish/', views.posts.publish, name='posts.publish'),
    path('drafts/', views.posts.DraftsView.as_view(), name='posts.drafts'),
]
