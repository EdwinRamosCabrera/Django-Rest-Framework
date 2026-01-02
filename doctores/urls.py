from django.urls import path
from .views import doctor_list, doctor_detail, create_doctor, update_doctor, delete_doctor, modify_doctor

urlpatterns = [
    path('doctores/', doctor_list, name='doctor-list'),
    path('doctor/<int:pk>/', doctor_detail, name='doctor-detail'),
    path('doctor/create/', create_doctor, name='create-doctor'),  
    path('doctor/update/<int:pk>/', update_doctor, name='update-doctor'),
    path('doctor/delete/<int:pk>/', delete_doctor, name='delete-doctor'),
    path('doctor/modify/<int:pk>/', modify_doctor, name='modify-doctor'),
]
