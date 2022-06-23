from importlib.resources import path
from django import views
from django.urls import URLPattern, path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from .views import combored, confirmapago, index ,mousepad,com_tec,selpago,confirmapago,carrito,combored,register


urlpatterns=[
    #urls de la aplicacion index
    path('',index,name="index"),
    path('mousepadRazer/',mousepad,name="mousepad"),
    path('combo-teclado/',com_tec,name="combo_teclado"),
    path('selpago/',selpago,name="selpago"),
    path('confirmapago/',confirmapago,name="confirmapago"),
    path('carrito/',carrito,name="carrito"),
    path('combored/',combored,name="combored"),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='core/logins/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='core/logins/logout.html'),name='logout'),
]