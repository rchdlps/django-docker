from django.urls import path
from . import views
from .views import (
    post_list_view,
    post_detail_view,
    post_create_view,
    post_update_view,
    post_delete_view,
    user_post_list_view
)

app_name = "blog"


urlpatterns = [
    path("", view=post_list_view, name='blog-home'),
    path("user/<str:username>", view=user_post_list_view, name='user-post'),
    path("post/<int:pk>/", view=post_detail_view, name='post-detail'),
    path("post/new/", view=post_create_view, name='post-create'),
    path("post/<int:pk>/update/", view=post_update_view, name='post-update'),
    path("post/<int:pk>/delete/", view=post_delete_view, name='post-delete'),
    path("about/", views.about, name='blog-about'),

]
