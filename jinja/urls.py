

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from website.views import Home,VerifyCertificate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('VerifyCertificate/',VerifyCertificate,name='verifycertificate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
