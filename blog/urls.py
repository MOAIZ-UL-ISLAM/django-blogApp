from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('blog/<slug:url>', views.posts, name='post'),
]
