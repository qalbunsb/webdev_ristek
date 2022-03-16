from .views import *
from django.urls import path

urlpatterns = [
	path('', index, name='index'),
    path('signup',signup,name='signup'),
    path('login',login_view,name='login'),
    path('logout',logout_view,name='logout'),
    path('profle',profile_view,name='profile'),
    path('author', author_view,name='author'),
]
