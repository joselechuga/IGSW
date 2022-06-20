from importlib.resources import path
from django.urls import URLPattern, path
from .views import index ,log,mousepad,com_tec,form_registrousu


urlpatterns=[
    #urls de la aplicacion index
    path('',index,name="index"),
    path('login/',log,name="login"),
    path('mousepadRazer/',mousepad,name="mousepad"),
    path('combo-teclado/',com_tec,name="combo_teclado"),
    path('form_registrousu/',form_registrousu,name="form_registrousu"),
]