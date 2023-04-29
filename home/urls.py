from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.index,name='Home'),
    path('about',views.about,name='About'),
    path('doctors',views.doctors,name='Doctors'),
    path('department',views.department,name='Department'),
    path('booking',views.booking,name='Booking'),
    path('contact',views.contact,name='Contact'),
]
