from django.contrib import admin
from .models import CategoryList,Item,VideoComment
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
     pass


# Register your models here.
admin.site.register((CategoryList,VideoComment))
# admin.site.register(Article)
admin.site.register(Item,MyModelAdmin)
