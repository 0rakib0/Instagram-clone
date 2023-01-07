from django.contrib import admin
from django.urls import path, include
from Post_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('Auth_app.urls')),
    path('post/',include('Post_app.urls')),
    path('', views.Home, name='home')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
