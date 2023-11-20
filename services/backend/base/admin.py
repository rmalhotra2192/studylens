from django.apps import apps
from django.contrib import admin
from .models import *

app_models = apps.get_app_config("base").get_models()

for model in app_models:
    admin.site.register(model)
