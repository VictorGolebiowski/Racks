from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def solutions(request):
    return render(request, 'solutions.html', {})


def portfolio(request):
    return render(request, 'portfolio.html', {})


def portfolio_single(request):
    return render(request, 'portfolio-single.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    return render(request, 'contact.html', {})


