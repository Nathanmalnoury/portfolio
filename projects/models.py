import mistune as mistune
from django.db import models


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=25)
    link = models.URLField(blank=True)

    def __str__(self):
        return f'{self.title}'


class Project(models.Model):
    title = models.CharField(max_length=50)
    meta = models.CharField(max_length=110)
    description = models.TextField()
    image = models.ImageField(upload_to='img/')
    tag = models.ManyToManyField(Tag)
    link = models.URLField(blank=True)

    def get_html_description(self):
        return mistune.markdown(self.description)

    def __str__(self):
        return f'{self.title}'
