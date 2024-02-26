from django.urls import path
from . import views
urlpatterns = [
    path('',views.polls,name='myname'),
    path('ff/<str:pk>',views.about,name='ffn'),
    path('create/',views.forms,name='myform'),
    path('edit/<str:pk>',views.edit,name='editn'),
    path('delete/<str:pk>',views.delete,name='deleten'),
    path('login/',views.loginpage,name='myuser'),
    path('logout/',views.logoutpage,name='myout'),
    path('register/',views.registerpage,name='register'),
    path('deletemsg/<str:pk>',views.deletemsg,name="delmsg"),
    path('profile/<str:pk>',views.profile,name="profile")

]