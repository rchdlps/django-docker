from django.urls import path

from . import views


app_name = "board"
urlpatterns = [
    path('boards/', views.BoardListView.as_view(), name="board_list"),
]
