from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.index , name="profilepage"),
    path('about/', views.about , name="aboutpage"),
    path('permission/', views.permissionpage , name="permissionpage"),
]
