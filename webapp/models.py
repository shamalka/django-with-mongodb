from django.db import models

# Create your models here.
class employees(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstName