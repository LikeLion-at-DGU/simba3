from django.contrib import admin
from .models import Post,TrackKey,FieldKey,Apply
# Register your models here.
admin.site.register(Post)
admin.site.register(FieldKey)
admin.site.register(TrackKey)
admin.site.register(Apply)

