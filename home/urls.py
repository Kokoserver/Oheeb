
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home" ),
    path('contact', views.contact, name="contact" ),
    path('about', views.about, name="about" ),
    path('accesspoint', views.accesspoint, name="accesspoint" ),
    path('desktop', views.desktop, name="desktop" ),
    path('monitor', views.monitor, name="monitor" ),
    path('motherboard', views.motherboard, name="motherboard" ),
    path('camera', views.camera, name="camera" ),
    path('search', views.search, name="search" ),
    path('<int:id>/product', views.product, name="product" ),
    path('<int:id>/cart', views.cart, name="cart" )
]