from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=150)
    date=models.DateField()
    description=models.TextField(max_length=300)

    
    def __str__(self):
        return self.title

