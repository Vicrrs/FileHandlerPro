from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('upload-form/', views.upload_file_form, name='upload_file_form'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]
