from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('news_detail/<int:pk>', views.newsDetailView.as_view(), name='news_detail'),

    path('category_detail/<int:pk>',
         views.catDetailView.as_view(), name='category_detail'),
    path('publisher_detail/<int:pk>',
         views.pubDetailView.as_view(), name='publisher_detail'),
    path('add', views.add, name='add'),
]
