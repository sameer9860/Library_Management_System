from django.urls import path
from . import views  # Assuming views.py is in the same app directory

urlpatterns = [
    path('', views.index, name='index'),  # Root URL points to index view
]