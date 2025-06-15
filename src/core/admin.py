from django.contrib import admin
from core.models import Pessoa

# Registers the Pessoa model with the Django admin site,
# allowing it to be managed through the admin interface.
admin.site.register(Pessoa)