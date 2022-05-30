from django.db import models
from .utlis import cover_directory_path
from tinymce.models import HTMLField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    cover = models.ImageField(upload_to=cover_directory_path, blank=True, null=True)
    body = HTMLField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        if self.pk:
            this_record = Post.objects.get(id=self.id)
            if this_record.cover != self.cover:
                this_record.cover.delete(save=False)
        super(Post, self).save(*args, **kwargs)
