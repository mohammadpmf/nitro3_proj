from django.contrib import admin

from . import models

admin.site.register(models.GenreMovie)
admin.site.register(models.GenreMusic)
admin.site.register(models.Artist)
admin.site.register(models.Movie)
admin.site.register(models.Serial)
admin.site.register(models.Music)
admin.site.register(models.Image)
admin.site.register(models.Staff)