from django.urls import path
from app import views
urlpatterns = [path('singup/', views.show, name='singup'),
path('log/', views.log, name='login'),
path('profile/', views.profile, name='profile'),

]