from django.db import models
from django.contrib.auth.models import User



class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ManyToManyField("Category")
    publisher = models.ManyToManyField("Publisher")
    is_publisher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.category


class Publisher(models.Model):
    publisher = models.CharField(max_length=150)

    def __str__(self):
        return self.publisher

class News(models.Model):
    title = models.CharField(max_length=400)
    short_desc = models.CharField(max_length=600)
    published = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    description = models.CharField(max_length=10000, null=True, blank=True)
    pictures = models.ImageField(
        null=True, blank=True, upload_to='news_images')

    def __str__(self):
        return self.title
