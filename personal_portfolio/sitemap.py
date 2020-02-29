from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from projects.models import Project
from aboutme.models import Section


class SectionSiteMap(Sitemap):
    def items(self):
        return Section.objects.all()

class AboutMeSiteMap(Sitemap):
    def items(self):
        return ['contact', 'mail']

    def location(self, item):
        return reverse(item)

class ProjectSiteMap(Sitemap):
    def items(self):
        return Project.objects.all()

