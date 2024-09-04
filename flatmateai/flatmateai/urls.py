from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create the schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Faltemate Djnago APIs",
        default_version='v1',
        description="Faltemate Django API testing and documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@nhancio.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Your other URL patterns
    path('api/', include('User.urls')),  # Replace with your app's URL configuration

    # Swagger UI endpoints
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
]
