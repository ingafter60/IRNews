from django.contrib import admin
from news.models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
	list_display = ('text', 'created_on', 'total_likes')
	list_filter = ['created_on']
	search_fields = ['text']

admin.site.register(News, NewsAdmin)
