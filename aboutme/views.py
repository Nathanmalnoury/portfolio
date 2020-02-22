from django.shortcuts import render

# Create your views here.
from aboutme.models import Section


def section(request):
    context = {
        'sections': Section.objects.all,
    }
    return render(request, 'aboutme.html', context=context)
