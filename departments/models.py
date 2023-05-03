from django.db import models

# Create your models here.


class department(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(
        max_length=1000)
    image = models.ImageField(upload_to="images")
    total_students = models.CharField(max_length=5, default="")

    def __str__(self):
        return self.title


class faculty(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images', default="")
    job_profile = models.CharField(max_length=100, default="")
    area_of_interest = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email_id = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name
