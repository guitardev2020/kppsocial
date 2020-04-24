from django.urls import path

from . import views

urlpatterns = [
    # ex: /kppdata
    path('', views.index, name='index'),
 
]