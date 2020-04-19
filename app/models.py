from django.db import models

# Create your models here.
sem=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
class Personaldetails(models.Model):
    name=models.CharField(max_length=20)
    register_no=models.CharField(primary_key=True,max_length=40)
    year=models.IntegerField()
    semister=models.CharField(max_length=2,choices=sem,default='1')
    cgpa=models.IntegerField()
    ph_no=models.IntegerField()
