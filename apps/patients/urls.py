from django.urls import path
from . import views

app_name = 'patients'
urlpatterns = [
    
    path('patient_profile/', views.patient_profile, name='profile'),
    path("video_call/", views.video_call, name='video call'),
    path("meeting/", views.meeting, name='meeting'),
    path('patient_login/', views.patient_login, name='patient_login'),
    path('patient_edit/', views.patient_edit, name='patient_edit'),

]