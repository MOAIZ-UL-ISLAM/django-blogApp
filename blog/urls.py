from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('<slug:url>', views.posts, name='post'),
]
