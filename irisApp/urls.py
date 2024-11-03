from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_home, name='model_home'),
    # path('predict/', views.predict, name='predict'),
]