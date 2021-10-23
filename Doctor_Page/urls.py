
from django.contrib import admin
from django.urls import path
from Doctor_Page import views

urlpatterns = [
    path("visit profile", views.visit_profile, name='visit profile'),
    path("partner with us", views.partner_with_us, name='partner with us'),
    path("video call", views.video_call, name='video call')
]
