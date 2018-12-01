from django.db import models

from django.utils import timezone
# Create your models here.

class Post(models.Model):
	
	author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	visitas = models.IntegerField()
	image = models.ImageField(verbose_name="image", upload_to = "blog")
	#visitas = 0 
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
	
	def contar_visita(self):
		 self.visitas = self.visitas + 1 
		 self.save()
	

#Creamos un modelo de comentarios 

class Comments(models.Model):
	
	post = models.ForeignKey('blog.Post',on_delete = models.CASCADE, related_name='comments')
	author = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	approved_comment = models.BooleanField(default = False)
	
	def approved(self):
	
		self.approved_comment = True 
		self.save()

	def __str__(self):
		return self.text
	
	def approved_comments(self):
		return self.objects.filter(approved_comment=True)
		


#Modelo de autor, muy parecido al post 

class Autor(models.Model):
		
		name = models.CharField(max_length = 50)
		description = models.TextField()
		image = models.ImageField(upload_to = "blog", verbose_name="image")
		author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
		
		def __str__(self):
		
			return self.name
		
		

		

		