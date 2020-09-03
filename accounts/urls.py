from django.urls import path, include

from knox.views import LogoutView

from .views import UserAPIView, RegisterAPIView, LoginAPIView

#url patterns for all account functions
urlpatterns = [
    path('', include('knox.urls')),
    path('user/<int:pk>', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout')
]