from django.urls import path
from .views import *

urlpatterns = [
   # path('',new_post),
    path('',index),
    path('about/',about, name = 'about'),
    path('create_post/',create_new_post, name = 'create_post'),
    path('get_post/<int:post_id>/',get_one_post, name = 'get_post'),
    path('get_all_posts/', posts, name='all_posts'),
]
