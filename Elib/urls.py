from Elib import views
from django.urls import path,include
urlpatterns=[
path('',views.index,name='index'),
path('home',views.home,name='home'),
path('login',views.loginuser,name='login'),
path('register',views.register,name='register'),
path('logout',views.logout,name='logout'),
path('book_view/<slug>',views.book_view,name='book_view'),

]