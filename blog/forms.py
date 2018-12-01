#Creamos un formulario para nuestro modelo Post 
from django import forms
from .models import Post, Comments , Autor



#Creamos un modelo de formulario 
class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text','image',)


class CommentForm(forms.ModelForm):
			
	class Meta:
		model = Comments
		fields=('author','text',)


class AutorForm(forms.ModelForm):
	
	class Meta:
		model = Autor
		fields = ('name', 'description', 'image')