from django.db import models

from django.utils import timezone
# Create your models here.

#Modelo de categorias 

class Category(models.Model):

	name = models.CharField(max_length = 50,verbose_name="Nombre")
	created = models.DateTimeField(auto_now_add = True ,verbose_name = "Fecha de creación")
	updated = models.DateTimeField(auto_now = True ,verbose_name = "Fecha de creación")

	class Meta: 
		verbose_name = "Categoría"
		verbose_name_plural = "Categorías"

	def __str__(self):
		
		return self.name

class Post(models.Model):
	
	author = models.ForeignKey('auth.User',on_delete = models.CASCADE, verbose_name = "Autor")
	title = models.CharField(max_length = 200, verbose_name = "Titulo")
	text = models.TextField(verbose_name = "Texto")
	created_date = models.DateTimeField(default = timezone.now , verbose_name = "Fecha de creación")
	published_date = models.DateTimeField(blank = True, null = True, verbose_name = "Fecha de publicación")
	visitas = models.IntegerField(verbose_name = "Número de visitas", blank = True, null = True)
	image = models.ImageField( upload_to = "blog", verbose_name = "Imagen")
	categories = models.ManyToManyField(Category, verbose_name= "Categorías")
	#visitas = 0 
	
	class Meta: 
		verbose_name = "Entrada"
		verbose_name_plural = "Entradas"

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
	
	post = models.ForeignKey('blog.Post',on_delete = models.CASCADE, related_name='comments', verbose_name = "Entrada")
	author = models.CharField(max_length = 200 ,verbose_name = "Entrada")
	text = models.TextField(verbose_name = "Texto")
	created_date = models.DateTimeField(default = timezone.now,verbose_name = "Fecha de creación")
	approved_comment = models.BooleanField(default = False,verbose_name = "Comentario aprobado")
	
	class Meta: 
		verbose_name = "Comentario"
		verbose_name_plural = "Comentarios"

	def approved(self):
	
		self.approved_comment = True 
		self.save()

	def __str__(self):
		return self.text
	
	def approved_comments(self):
		return self.objects.filter(approved_comment=True)
		


#Modelo de autor, muy parecido al post 

class Autor(models.Model):
		
		name = models.CharField(max_length = 50,verbose_name="Nombre")
		description = models.TextField()
		image = models.ImageField(upload_to = "blog",verbose_name="Imagen")
		author = models.ForeignKey('auth.User',on_delete = models.CASCADE,verbose_name="Autor")
		
		class Meta: 
			verbose_name = "Creador"
			verbose_name_plural = "Creadores"

		def __str__(self):
		
			return self.name
			
		
