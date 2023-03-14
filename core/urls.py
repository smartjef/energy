from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('energy/',views.energy,name='energy'),
]