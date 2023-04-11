from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views
# from app import views
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/register/', RegistrationView.as_view(success_url='/create_profile'), name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path("checkout/", include("checkout.urls", namespace="checkout")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_then_login , name='logout'),
    
  
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
