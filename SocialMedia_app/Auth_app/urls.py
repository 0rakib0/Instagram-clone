from django.urls import path
from . import views
app_name = 'Auth_app'

urlpatterns = [
    path('Register/', views.Register, name='register'),
    path('login/', views.Login_page, name='login'),
    path('do-login/', views.Do_login, name='do_login'),
    path('user/profile/<id>/', views.Profile, name='profile'),
    path('user/update/profile/', views.Update_profile, name='update_profile'),
    path('user/add-more/upate', views.Add_more, name='Add_more'),
    path("user/more-info/update", views.Update_more, name="update_more"),
    path('logout/', views.Do_logout, name='logout'),
    path('other/user/<username>/', views.Other_userprofile, name='other_user'),
    path('follow/user/<username>/', views.Follow_user, name='follow_user'),
    path('unfollow/user/<username>/', views.Unfollow_user, name='unfollow_user'),
]
