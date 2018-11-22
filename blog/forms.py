#Creamos un formulario para nuestro modelo Post 
from django import forms
from .models import Post, Comments
#Creamos un modelo de formulario 
class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
			
	class Meta:
		model = Comments
		fields=('author','text',)
	