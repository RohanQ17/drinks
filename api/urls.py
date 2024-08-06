from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.jobs_api, name='jobs-list-create'),
    path('jobs/<str:id>/', views.jobs_api, name='jobs-detail'),
]