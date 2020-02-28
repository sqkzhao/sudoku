from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_game', views.new_game),
    # path('validate', views.validate),
    # path('board', views.board),
]
