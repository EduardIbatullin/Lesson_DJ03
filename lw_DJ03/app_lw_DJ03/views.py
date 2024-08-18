from django.shortcuts import render
from .models import News_post


def home(request):
    news = News_post.objects.all()
    return render(request, 'app_lw_DJ03/news.html', {'news': news})
# Create your views here.
