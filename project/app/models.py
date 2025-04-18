from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    views = models.IntegerField(null= True, blank=True)
    duration = models.IntegerField(null= True, blank=True)
    image = models.ImageField(upload_to='videos')

    def __str__(self):  
        return self.title
    
    def url_image(self):
        return self.image.url
