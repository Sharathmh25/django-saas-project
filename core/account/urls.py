
from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('register/',views.signup_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')
]
