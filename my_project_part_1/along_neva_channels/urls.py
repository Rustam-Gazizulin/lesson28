# TODO настраиваем urls здесь
from django.urls import path

from along_neva_channels import views

urlpatterns = [
    path('', views.TourListView.as_view(), name='Tours'),
    path('<int:pk>/', views.TourDetailView.as_view(), name='Tour'),

]
