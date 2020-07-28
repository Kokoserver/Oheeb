
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home" ),
    path('view/<int:id>', views.view, name="view" )
]