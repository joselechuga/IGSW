from importlib.resources import path
from django.urls import URLPattern, path
from .views import index ,log,mousepad,com_tec

urlpatterns=[
    path('',index,name="index"),
    path('login/',log,name="login"),
    path('mousepadRazer/',mousepad,name="mousepad"),
    path('combo-teclado/',com_tec,name="combo_teclado"),

]