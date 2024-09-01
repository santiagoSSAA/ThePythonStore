from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name='products'),
    path('health/', views.HealthCheckView.as_view(), name='health_check')
]