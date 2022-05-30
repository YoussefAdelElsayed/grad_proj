from django.db import models
from PIL import Image

# Create your models here.


class Degree(models.Model):
    Qualifi = models.CharField(max_length=100)
    Celsius =  models.CharField(max_length=100)
    def __str__(self):
        return str(self.Qualifi)



class Home(models.Model):
    slide = models.ImageField(upload_to="Home/slide")
    slide2 = models.ImageField(upload_to="Home/slide")
    slide3 = models.ImageField(upload_to="Home/slide")
    about =models.CharField(max_length=750)
    degree = models.ManyToManyField(Degree)
    Awarded = models.CharField(max_length=100)
    Awarded2 = models.CharField(max_length=100)
    coun=models.IntegerField()
    coun2=models.IntegerField()
    coun3=models.IntegerField()
    coun4= models.IntegerField()
    
    def save(self, *args, **kwargs):
        if self.pk:
            this_record = Home.objects.get(id=self.id)
            
            if this_record.slide != self.slide:
                this_record.slide.delete(save=False)
            
            elif this_record.slide2 != self.slide2:
                    this_record.slide2.delete(save=False)
            
            elif this_record.slide3 != self.slide3:
                    this_record.slide3.delete(save=False)
        
        
        super(Home, self).save(*args, **kwargs)
    
    @property
    def get_degree(self):
        return self.degree.all()