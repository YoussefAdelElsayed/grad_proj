from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Doctor
from tinymce.models import HTMLField
from .utils import slugify
import uuid
# Create your models here.

class Year(models.Model):
    title=models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Year, self).save(*args, **kwargs)

    @property
    def get_lectures(self):
        return self.lecture_set.all()


class Lecture(models.Model):
    title = models.CharField(max_length=250)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250,blank=True, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    video = models.FileField(upload_to='Lecture', validators=[FileExtensionValidator(allowed_extensions=['mp4'])],blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            this_record = Lecture.objects.get(id=self.id)
            if this_record.video != self.video:
                this_record.video.delete(save=False)
            
        if not self.slug:
            url=str(uuid.uuid4())
            self.slug = slugify(f'{self.title[:10]}'+'-'+url.split('-')[1])
        super(Lecture, self).save(*args, **kwargs)

