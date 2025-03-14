"""
URL configuration for roomBooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from .views import RoomList,BookingList,BookingView, cancel_booking

app_name = "roomBooking"

def redirect_to_login(request):
    return redirect('account_login')  # 'account_login' is the default login URL in allauth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room_list/', RoomList.as_view(), name ='RoomList'),
    path('booking_list/', BookingList.as_view(), name ='BookingList'),
    path('book/', BookingView.as_view(), name = 'booking_view'),
    path('accounts/', include('allauth.urls')),
    path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('', redirect_to_login)
]
