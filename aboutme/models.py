import mistune
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)


# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag, blank=True)
    description = models.TextField()
    meta = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.title)

    def get_html_description(self):
        return mistune.markdown(self.description)

    def get_absolute_url(self):
        return "/section/%i/" % self.id
