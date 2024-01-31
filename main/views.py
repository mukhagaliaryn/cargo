from django.shortcuts import render, get_object_or_404
from .models import Offer, Business, Logistic


def main(request):
    offers = Offer.objects.all()
    businesses = Business.objects.all()
    logistics = Logistic.objects.all()

    context = {
        'offers': offers,
        'businesses': businesses,
        'logistics': logistics
    }
    return render(request, 'main/index.html', context)


def news(request):
    businesses = Business.objects.all()
    logistics = Logistic.objects.all()

    context = {
        'businesses': businesses,
        'logistics': logistics
    }
    return render(request, 'main/news.html', context)


def about(request):
    businesses = Business.objects.all()
    logistics = Logistic.objects.all()

    context = {
        'businesses': businesses,
        'logistics': logistics
    }
    return render(request, 'main/about/index.html', context)


def about_corp(request):
    businesses = Business.objects.all()
    logistics = Logistic.objects.all()

    context = {
        'businesses': businesses,
        'logistics': logistics
    }
    return render(request, 'main/about/corp.html', context)


def about_org(request):
    businesses = Business.objects.all()
    logistics = Logistic.objects.all()

    context = {
        'businesses': businesses,
        'logistics': logistics
    }
    return render(request, 'main/about/org.html', context)


def business_detail(request, pk):
    business = get_object_or_404(Business, pk=pk)

    businesses = Business.objects.all()
    logistics = Logistic.objects.all()

    context = {
        'business': business,

        'businesses': businesses,
        'logistics': logistics
    }
    return render(request, 'main/business/index.html', context)


def logistic_detail(request, pk):
    logistic = get_object_or_404(Logistic, pk=pk)

    businesses = Business.objects.all()
    logistics = Logistic.objects.all()
    context = {
        'logistic': logistic,

        'businesses': businesses,
        'logistics': logistics
    }
    return render(request, 'main/logistic/index.html', context)
