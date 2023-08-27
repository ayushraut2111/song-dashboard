from django.db import models
import os
from django.dispatch import receiver


class songs(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    duration = models.FloatField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    extension = models.CharField(max_length=20, blank=True, null=True)
    audio = models.FileField(upload_to='songs')

    def __str__(self) -> str:
        return self.name


# this signal will automatically deletes the songs from the local storage also whenever object is deleted from the database
@receiver(models.signals.post_delete, sender=songs)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.audio:
        if os.path.isfile(instance.audio.path):
            os.remove(instance.audio.path)
