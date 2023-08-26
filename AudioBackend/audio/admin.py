from django.contrib import admin
from .models import songs

@admin.register(songs)
class SongRegister(admin.ModelAdmin):
    list_display=['id','name','date']
