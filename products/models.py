from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    name = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})

    def get_absolute_class_url(self):
        return reverse("products-class:detail", kwargs={"pk": self.pk})