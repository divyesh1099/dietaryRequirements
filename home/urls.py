from django.urls import path
from . import views
app_name='home'

urlpatterns=[
    path('', views.index, name='index'),
    path('invitation/', views.invitation, name='invitation'),
    path('summary/', views.summary, name='summary'),
    path('register/', views.register_superadmin, name='register'),
    path('login/', views.login_superadmin, name='login'),
    path('logout/', views.logout_superadmin, name='logout'),

]