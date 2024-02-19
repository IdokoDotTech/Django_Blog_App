from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    body = models.TextField()
    author = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(category, related_name="category")

    def __str__(self):
        return self.title