from django.shortcuts import render
from .models import Business


def main(request):
    businesses = Business.objects.all()
    context = {
        'businesses': businesses
    }
    return render(request, 'main/index.html', context)
