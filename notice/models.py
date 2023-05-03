from django.db import models

# Create your models here.


class notice(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to="notices")

    def __str__(self):
        return self.title
