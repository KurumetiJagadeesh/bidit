from django.urls import path
from . import views

urlpatterns=[
    path('',views.basic,name='basic'),
    path('home',views.home,name='home'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('product',views.product,name='product'),
    path('addbidding',views.addbidding,name='addbidding'),
    path('product1',views.product1,name='product1'),
    path('addbidding1',views.addbidding1,name='addbidding1'),
    path('product3',views.product3,name='product3'),
    path('product4',views.product4,name='product4'),
    path('addbidding3',views.addbidding3,name='addbidding3'),
    path('addbidding4',views.addbidding4,name='addbidding4'),
    path('product5',views.product5,name='product5'),
    path('addbidding5',views.addbidding5,name='addbidding5'),
    path('product6',views.product6,name='product6'),
    path('addbidding6',views.addbidding6,name='addbidding6'),
    path('product7',views.product7,name='product7'),
    path('addbidding7',views.addbidding7,name='addbidding7'),

]