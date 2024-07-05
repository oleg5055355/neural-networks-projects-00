from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Publisher)
admin.site.register(models.News)
admin.site.register(models.userProfile)
