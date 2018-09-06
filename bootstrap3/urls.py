from django.urls import path
from bootstrap3 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('post/', views.post, name='post'),
]
