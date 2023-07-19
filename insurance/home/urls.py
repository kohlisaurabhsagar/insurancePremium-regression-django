from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('prediction', views.prediction, name='prediction'),
]