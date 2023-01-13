# TODO настраиваем urls здесь
from django.urls import path

from moderation import views

urlpatterns = [
    path('listreview/', views.ReviewListView.as_view(), name='review'),
    path('feedback-delete/<int:pk>/', views.ReviewDeleteView.as_view(), name='delete'),
]
