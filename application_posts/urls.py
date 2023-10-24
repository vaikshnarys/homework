from django.urls import path
from .views import *
from .views_our import *
urlpatterns = [
    path('',index),
    path('about/',about, name = 'about'),
    path('get_post/<int:_id>/',get_orm_posts, name = 'get_post'),
    path('posts/', Get_post.as_view(), name='post_posts'),
    path('orm_posts/<int:_id>/', Update_delete_post.as_view(), name='orm_posts'),
    path('transaction/', Transaction.as_view(), name='transaction'),
    path('pageNotFound/', pageNotFound, name='pagenotfound'),
    path('check_is_exists/<int:_id>/',check_is_exists, name='check_is_exists'),
    path('get_or_create_post/<int:counter>/',get_orm_post_or_create, name = 'get_orm_post_or_create'),
    path('comments/',create_comment, name = 'create_comment'),
    path('get_comments/<int:post_id>',get_comments, name = 'get_comments'),
    path('change_status/<int:post_id>/<slug:status>',change_status_all_new, name = 'change_comments'),
]
