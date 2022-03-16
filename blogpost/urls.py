from django.urls import path
from .views import *
urlpatterns = [
    path('create', add_post,name = 'create_post'),
    path('', view_post, name = 'view_post_default'),
    path('<int:pk>/',view_post,name='view_post'),
    path('category/<str:name>/',view_category_post,name='category_posts')
]