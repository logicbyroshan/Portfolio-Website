from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This could be the home view for myapp
]
