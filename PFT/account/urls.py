from django.urls import path
from . import views

# Creating my routing table

urlpatterns = [
    path('',views.login, name='signin'),
    path('signup/',views.signup, name='signup')
]

