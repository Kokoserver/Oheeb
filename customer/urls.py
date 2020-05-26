
from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name="login" ),
    path('register', views.register, name="register" ),
    path('logout', views.logout, name="logout" ),
    path('helpCenter', views.helpCenter, name="helpCenter" ),
    path('dashboard', views.dashboard, name="dashboard" ),

]