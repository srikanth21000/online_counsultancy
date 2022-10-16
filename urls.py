from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.loginpage,name="login"),
    path('register/',views.registerUser,name='register'),
    path('profile/',views.profile,name='profiles'),
    path('logout/',views.logoutUser,name="logout"),
    path('properties/',views.property,name="properties"),
    path('submit_properties/',views.submit,name="submit"),
    path('contact_us/',views.contact,name="contact"),
    path('muzamil/',views.muzamil,name='muzamils'),
    path('muzamillog/',views.muzamillog,name='muzamillogs')
]
