from django.db import models

from django.utils import timezone
# Create your models here.

class Post(models.Model):
	
	author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title

		
#Creamos un modelo de comentarios 

class Comments(models.Model):
	
	post = models.ForeignKey('blog.Post',on_delete = models.CASCADE, related_name='comments')
	author = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now())
	approved_comment = models.BooleanField(default = False)
	
	def approved(self):
	
		self.approved_comment = True 
		self.save()

	def __str__(self):
		return self.text
	
	def approved_comments(self):
		comentarios = self.comments.filter(approved_comment=True)
		return comentarios.count()
		