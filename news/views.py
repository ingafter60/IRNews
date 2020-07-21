from django.shortcuts import render
from django.views import generic

from .models import News

# Create your views here.
# def home(request):
# 	return render(request, 'news/home.html', {'message': 'Hello world news!'})


class IndexView(generic.ListView):
    template_name = 'news/home.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.order_by('-created_on')[:20]


class DetailView(generic.DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'news'