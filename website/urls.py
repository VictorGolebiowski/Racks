from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('solutions.html', views.solutions, name="solutions"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('portfolio-single.html', views.portfolio_single, name="portfolio-single"),
    path('blog.html', views.blog, name="blog"),
    path('contact.html', views.contact, name="contact"),
]


