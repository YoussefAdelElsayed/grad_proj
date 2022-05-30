from django.db import models
from edu.models import Year
# Create your models here.


class Student(models.Model):
    name = models.CharField( max_length=150)
    sitting_number=models.IntegerField()
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    @property
    def get_result(self):
        return self.result_set.all()

    def __str__(self):
        return str(self.name)



class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    rating = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return str(self.student)
