from django.db import models

class Blogs(models.Model):
    tittle = models.CharField(max_length = 200)
    discription = models.TextField(max_length = 200)
    date = models.DateField()

    def __str__(self):
        return self.tittle
