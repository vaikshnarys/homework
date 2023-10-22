from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('about/',about, name = 'about'),
    path('create_post/',create_new_post, name = 'create_post'),
    path('get_post/<int:_id>/',get_orm_posts, name = 'get_post'),
    path('get_all_posts/', get_all_posts, name='get_all_posts'),
    path('pageNotFound/', pageNotFound, name='pagenotfound'),
    path('check_is_exists/<int:_id>/',check_is_exists, name='check_is_exists'),
    path('get_or_create_post/<int:counter>/',get_orm_post_or_create, name = 'get_orm_post_or_create'),
    path('delete_orm_post/<int:_id>/', delete_orm_post, name='delete_orm_post'),
    path('update_or_create_post/<int:_id>/',update_orm_post_or_create, name = 'get_orm_post_or_create'),
    path('comments/',create_comment, name = 'create_comment'),
    path('get_comments/<int:post_id>',get_comments, name = 'get_comments'),
    path('change_status/<int:post_id>/<slug:status>',change_status_all_new, name = 'change_comments'),
]
