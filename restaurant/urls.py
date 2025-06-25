from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
<<<<<<< HEAD
    path('menu/', views.menu, name='menu'),
=======
    # Add the remaining URL path configurations here
>>>>>>> 49ddca9892d8ce8080d3c1e09a4d79bda59804d4
]