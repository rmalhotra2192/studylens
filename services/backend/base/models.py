from django.db import models
from resources.models import Resource


# Create your models here.
class ExternalDataProviders(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    logo = models.CharField(max_length=512, null=True)


class ExternalUrls(models.Model):
    SERVICE_TYPES = [
        ("resource-purchase", "Resource Purchase"),
        ("resource-view", "Resource View"),
    ]

    url = models.CharField(max_length=512)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    external_provider = models.ForeignKey(
        ExternalDataProviders, on_delete=models.CASCADE
    )
    external_provider_service_type = models.CharField(
        choices=SERVICE_TYPES, max_length=128, null=True
    )


class ExternalMetrics(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    external_provider = models.ForeignKey(
        ExternalDataProviders, on_delete=models.CASCADE
    )
    external_provider_metric_category = models.CharField(
        max_length=128, null=True
    )  # e.g. "ratings, engagement, etc."
    external_provider_metric_key = models.CharField(
        max_length=128, null=True
    )  # e.g. "views, likes, etc."
    external_provider_metric_type = models.CharField(
        max_length=128, null=True
    )  # e.g. "integer, float, etc."
    external_provider_metric_value = models.CharField(
        max_length=128, null=True
    )  # e.g. "4.5, 100, etc."
    external_provider_metric_max = models.CharField(
        max_length=128, null=True
    )  # e.g. "5, 100, etc."
