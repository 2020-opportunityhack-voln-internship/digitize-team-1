from django.urls import include, path
from rest_framework import routers
from . import views

"""
URL Config for Form Upload API. 
"""

urlpatterns = [
    path('upload/', views.PaperFormUploadView.as_view(), name= 'paper_form'),
    path('paperform/<int:pk>/update', views.PaperFormUpdateView.as_view(), name='paper_form_update'),
    path('paperform/<int:pk>/delete', views.PaperFormDeleteView.as_view(), name='paper_form_delete'),

]