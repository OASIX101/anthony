from django.urls import path
from . import views

urlpatterns = [
    path('you/', views.test),
    path('frontpage/',views.frontpage),
    path('<slug:slug>/', views.post_detail)
]