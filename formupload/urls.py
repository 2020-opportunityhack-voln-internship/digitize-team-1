from django.urls import include, path
from rest_framework import routers
from . import views

"""
URL Config for Form Upload API. 
"""

urlpatterns = [
    path('upload/', views.PaperFormUploadView.as_view(), name= 'paper_form'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]