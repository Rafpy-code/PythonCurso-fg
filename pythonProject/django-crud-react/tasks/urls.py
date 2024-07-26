from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks import views

# Todo este código genera el CRUD
# api versioning
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title="Tasks API")),
    path(
        "openapi/",
        get_schema_view(title="tasks", description="API for all things …"),
        name="openapi-schema",
    ),
]
