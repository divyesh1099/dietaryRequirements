from django.urls import path
from . import views
app_name='home'

urlpatterns=[
    path('', views.index, name='index'),
    path('invitation/', views.invitation, name='invitation'),
    path('summary/', views.summary, name='summary'),
]