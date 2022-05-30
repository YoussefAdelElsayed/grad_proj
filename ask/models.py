from django.db import models
from edu.models import Year
# Create your models here.
class Ask(models.Model):
    YEAR_CHOICES=(('الفرقة الاولة','الفرقة الاولة'),('الفرقة الثانية','الفرقة الثانية'),('الفرقة الثالثة','الفرقة الثالثة'),('الفرقة الرابعة','الفرقة الرابعة'))
    name = models.CharField(max_length=300)
    year=models.ForeignKey(Year, on_delete=models.SET_NULL,blank=True, null=True)
    message=models.TextField()
    answer = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


