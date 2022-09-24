from django.db import models


# Create your models here.

class Track(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Student(models.Model):
    fname = models.CharField(max_length=50,null=False,default="NotSet")
    lname = models.CharField(max_length=50, null=False, default="NotSet")
    age = models.IntegerField(null=False)
    student_track=models.ForeignKey(Track,on_delete=models.CASCADE)
    # student_exam=models.ForeignKey(Exams,on_delete=models.CASCADE,default="None")
    def __str__(self):
        return  self.fname+' '+self.lname+' '
    def graduate(self):
        if self.age >20:
            return True
        else:
            return False
    graduate.short_description='Graduation Status'
    graduate.boolean=True

