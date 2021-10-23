from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'doctors'
urlpatterns = [
    path('visit_profile/', views.booking, name='booking'),
    path('partner/', views.partner, name='partner_with'),
    path('blog/', views.blog, name='blog_view'),
    path('add_blog/', views.blog_add, name='add_blog'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('schedule/', views.schedule_meet, name='schedule_meet'),
    path('all_doc/', views.doctor, name='doctor'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)