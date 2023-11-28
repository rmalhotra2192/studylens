from django.apps import AppConfig
from elasticsearch_dsl.connections import connections
from django.conf import settings


class ResourcesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "resources"

    def ready(self):
        connections.configure(
            default={"hosts": settings.ELASTICSEARCH_DSL["default"]["hosts"]},
        )
