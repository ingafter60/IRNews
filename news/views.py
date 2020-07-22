from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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


class MyView(IndexView):

	def get_queryset(self):
		return News.objects.filter(created_by=self.request.user.id) \
			.order_by('-created_on')[:20]

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(MyView, self).dispatch(*args, **kwargs)			