
from django.contrib import admin
from django.urls import path, include
from account import urls as account
from category import urls as category
from job import urls as job
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(account)),
    path('category/', include(category)),
    path('job/', include(job)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)