from django.contrib import admin
from django.apps import apps
from .models import *

# Register all models in application
app = apps.get_app_config("application")

for model_name, model in app.models.items():
    admin.site.register(model)
