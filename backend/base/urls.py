from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add_userprofile/', views.add_userprofile, name='add_userprofile'),
    path('customer_profile/', views.CustomerProfileView.as_view(), name='customer_profile'),
    path('seller_profile/', views.SellerProfileView.as_view(), name='seller_profile'),
    path('add_service/', views.add_service, name='add_service'),
     path('pics_posts/', views.PicsPostsView.as_view(), name='pics_posts'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('add_nextappointment/', views.add_nextappointment, name='add_nextappointment'),
]