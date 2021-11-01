from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.home),
  path('customer/', views.customer_page),
  path('courier/', views.courier_page),
]
