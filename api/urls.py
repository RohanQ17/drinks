from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.jobs_api, name='jobs-list-create'),
    path('jobs/<int:id>/', views.jobs_detail, name='jobs-detail'),
]