from django.urls import path
from . import views
urlpatterns = [
    path('' , views.started, name='index')
]