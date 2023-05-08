from django.db import models

class categories(models.Model):
    icon=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
# Create your models here.
