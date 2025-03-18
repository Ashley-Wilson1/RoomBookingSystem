from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from .views import RoomList, BookingList, BookingView, cancel_booking

def redirect_to_login(request):
    return redirect('account_login')  # Allauth login view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view'),
    path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    
    # Allauth routes for login, signup, etc.
    path('accounts/', include('allauth.urls')),
    
    # Redirect to login page if accessing the root
    path('', redirect_to_login),
]
