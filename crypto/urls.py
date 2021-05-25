from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('prices/', views.prices, name="prices") # the same action form in the base.html
]
