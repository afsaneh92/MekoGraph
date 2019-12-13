from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.index, name='main-view'),
    path('show_image', views.showimage, name='show'),]