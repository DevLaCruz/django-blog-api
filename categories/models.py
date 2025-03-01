from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250, unique=True)
    published=models.BooleanField(default=False)

    def __str__(self):
        return self.title