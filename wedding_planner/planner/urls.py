from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import BookServiceView, contact_admin

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/book/', views.BookServiceView.as_view(), name='book_service'),
    path('contact/', contact_admin, name='contact_admin'),
    path('portfolio/', views.portfolio, name='portfolio'),
    
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
