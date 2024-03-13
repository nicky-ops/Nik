from django.db import models
from django.contrib.flatpages.models import FlatPage

# Create your models here.
class SearchKeyword(models.Model):
    keyword = models.CharField(max_length=50, unique=True)
    page = models.ForeignKey(FlatPage, on_delete=models.CASCADE)

    def __str__(self):
        return self.keyword
