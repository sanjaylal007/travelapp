from . import views
from django.urls import path

urlpatterns = [

    path('',views.function,name='function'),
    path('2nd',views.function2,name='function2'),
    path('3rd',views.function3,name='function3'),
    path('add/',views.addition,name='addition')
]
