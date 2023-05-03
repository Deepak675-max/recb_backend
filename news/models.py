from django.db import models

# Create your models here.


class news(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to="news")

    def __str__(self):
        return self.title
