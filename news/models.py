from django.db import models

# Create your models here.
class News(models.Model):
	text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	via = models.URLField(blank=True)

	def total_likes(self):
		return self.like_set.count()

	class Meta:
		verbose_name = 'news'
		verbose_name_plural = 'news'	

class Like(models.Model):
	news = models.ForeignKey(News, on_delete=models.CASCADE)

