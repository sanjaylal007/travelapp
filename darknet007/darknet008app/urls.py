from . import views
from django.urls import path

urlpatterns = [

    path('dark',views.darknet,name='darknet'),
    ]
