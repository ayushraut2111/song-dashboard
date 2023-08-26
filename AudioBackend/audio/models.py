from django.db import models


class songs(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    duration=models.FloatField(blank=True,null=True)
    size=models.FloatField(blank=True,null=True)
    extension=models.CharField(max_length=20,blank=True,null=True)
    audio=models.FileField(upload_to='songs')
    # def __str__(self) -> str:
    #     return self.name
