from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('house/<int:house_id>/', views.house_detail, name='house_detail'),
    path('book/<int:house_id>/', views.book_house, name='book_house'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('invoice/<int:booking_id>/', views.view_invoice, name='view_invoice'),
     path('complain/', views.complain_page, name='complain_page'),
     path('submit/', views.submit_payment, name='submit_payment'),
   
]
