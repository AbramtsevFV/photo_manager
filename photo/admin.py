from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_html_previewImg', 'date_load')
    list_filter = ('user',)
    list_display_links = ('id', 'user')
    search_fields = ('name',)

    def get_html_previewImg(self, object):
        if object.photo:
            return mark_safe(f"<img src = {object.photo.url} width=30>")

    get_html_previewImg.short_description = 'Фото'


class UserNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Photo, PhotoAdmin)
admin.site.register(UserName, UserNameAdmin)
