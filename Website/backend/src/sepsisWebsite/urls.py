from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('profiles_api.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('sepsisAPI/', include('sepsisAPI.urls'))
]
