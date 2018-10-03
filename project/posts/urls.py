from django.urls import path

from . import views


app_name = "posts"
urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
]
