from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('',views.Home,name="Home"),
    path('login',views.LoginHandle,name='LoginHandle'),
    path('SignUp',views.SignHandle,name='SignHandle'),
    path('logout',views.LogoutHandle,name='LogoutHandle'),
    path('MyProfile',views.Profile,name='Profile'),
    path('post/<str:Slug>',views.HandlePost,name='HandlePost'),
    path('contact',views.contact_us,name="contact_us"),
    path("read/prince_of_persia",views.pop,name="pop"),
    path('read/red_dead_redemption_2',views.red,name='red'),
    path('read/Assassins-Creed',views.assassins,name='assassins'),
    path('SendOtp',views.SendOtp,name='SendOtp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

