from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Film app Rest API",
        default_version="v1",
        description="Swagger docs Rest API",
        contact=openapi.Contact("ALisher Shamuratov <shamuratov0002@gmail.com>"),
    ),
    public=True,
    permission_classes=(AllowAny,)
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('film.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
