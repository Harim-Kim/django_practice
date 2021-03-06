from django.urls import path
from bookmark.views import *

app_name = 'bookmark'
urlpatterns = [
    path('bookmark/', BookmarkLV.as_view(), name='index'),
    path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
