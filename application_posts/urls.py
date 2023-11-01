from django.urls import path
from .views import *
from .views_our import *
urlpatterns = [
    path('',index),
    path('about/',about, name = 'about'),
    path('get_post/<int:_id>/',get_orm_posts, name = 'get_post'),
    path('orm_posts/<int:_id>/', Update_delete_post.as_view(), name='orm_posts'),
    path('transaction/', Transaction.as_view(), name='transaction'),
    path('pageNotFound/', pageNotFound, name='pagenotfound'),
    path('check_is_exists/<int:_id>/',check_is_exists, name='check_is_exists'),
    path('get_or_create_post/<int:counter>/',get_orm_post_or_create, name = 'get_orm_post_or_create'),
    path('comments/',create_comment, name = 'create_comment'),
    path('get_comments/<int:post_id>',get_comments, name = 'get_comments'),
    path('change_status/<int:post_id>/<slug:status>',change_status_all_new, name = 'change_comments'),

    path('wallets/', Walletview.as_view(), name='wallets'),
    path('wallets/<int:_id>/', DetailWallet.as_view(), name='wallet'),
    path('wallets/form/', FormRender.as_view(), name='wallet_form'),
    path('wallets/edit/<int:_id>/', EditWalletView.as_view(), name='wallet_edit'),
    path('wallets/edit/form/<int:_id>/', EditFormRender.as_view(), name='edit_wallet_form'),
    path('wallets/delete/<int:_id>', DeleteWallet.as_view(), name='wallet_delete'),
]
