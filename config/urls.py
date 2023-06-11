import os

"""Main URLs module."""
from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
# drf_yasg code starts here
from rest_framework import permissions       # type: ignore
from drf_yasg.views import get_schema_view   # type: ignore
from drf_yasg import openapi                 # type: ignore
from rest_framework import routers
# Api router
router = routers.DefaultRouter()

# drf_yasg code starts here
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Welcome to Blog",
        terms_of_service="https://www.linkedin.com/in/carlos-daniel-visbal-atencia-4a713b114",
        contact=openapi.Contact(email="carlosvisbal66@gmail.com"),
        license=openapi.License(name="Blog Django"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ends here

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  #<-- Here
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  #<-- Here
    # Django Admin
    path('admin/', admin.site.urls),
    # Api routes
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.blog.urls')),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)