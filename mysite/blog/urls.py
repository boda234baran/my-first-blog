from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    #name='post_list' — это имя URL, которое будет исп1ользовано, чтобы идентифицировать его.
    #Оно может быть таким же, как имя представления (англ. view), а может и чем-то совершенно другим
]
