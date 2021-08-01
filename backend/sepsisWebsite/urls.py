from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api-auth/', include('profiles_api.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    # path('sepsisWebSocket/', include('sepsisDynamic.urls')),
    path('sepsisAPI/', include('sepsisAPI.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
