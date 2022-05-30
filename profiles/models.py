from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Department (models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_doctors(self):
        return self.doctor_set.all()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='professorPhoto', default='user.png')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk:
            this_record = Doctor.objects.get(id=self.id)
            if this_record.photo != self.photo:
                this_record.photo.delete(save=False)
        if not self.slug:
            self.slug = slugify(str(self.user))
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.fullName)

