from django.contrib import admin

# Register your models here.
from aboutme.models import Section, Tag


class SectionAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Section, SectionAdmin)
admin.site.register(Tag, TagAdmin)
