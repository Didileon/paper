from django.contrib import admin
#from django.contrib.sitemaps.views import index
from django.urls import path
from .views import PostsList, PostDetail

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
