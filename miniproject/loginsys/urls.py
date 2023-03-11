from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('category/<str:value>',views.category,name="dairy"),
    #path('category/<str:featuredindex>',views.index,name="indeximgages"),
    path('logout',views.logout,name='logout'),
    path('index',views.home,name="home"), 
    path('add_to_cart',views.add_to_cart,name="add"),
    path("cart", views.cart, name="cart"),
    path("delete_item", views.delete_item, name="add")
]