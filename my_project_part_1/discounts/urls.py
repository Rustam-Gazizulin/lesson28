# TODO настраиваем urls здесь
from django.urls import path

from discounts import views

urlpatterns = [
    path('', views.DiscountListView.as_view(), name='discount'),
    path('<int:pk>/', views.DiscountDetailView.as_view(), name='discount_id'),
]
