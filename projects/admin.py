from django.contrib import admin

# Register your models here.
from projects.models import Project, Tag


class ProjectAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)