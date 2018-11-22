from django.shortcuts import render,get_object_or_404
from .models import Post,Comments
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def post_list(request):
	
	#Obtenemos la lista de Posts publicados por fecha de publicación 
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	#Los mostramos 
	return render(request, 'blog/post_list_blog.html', {'posts':posts})

def post_list_new(request):
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-created_date')
	return render(request, 'blog/post_list_blog_new.html', {'posts':posts})
	

def post_detail_blog(request, pk):
	
	post = get_object_or_404(Post,pk = pk)
	return render(request, 'blog/post_detail_blog.html', {'post' : post})
	
@login_required	
def post_new(request):
	#Para guardar el post creado
	if request.method == "POST":
		#los campos del formulario están ahora en request.post 
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			#redirigimos al post 
			return redirect('post_detail_blog', pk = post.pk)
	else:		
			
		form = PostForm()

		return render(request, 'blog/post_edit.html',{'form':form })
	
@login_required	
def post_edit(request, pk):
	post = get_object_or_404(Post, pk = pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			return redirect('post_detail_blog', pk = post.pk)
	else:
		form = PostForm(instance = post)
		return render(request, 'blog/post_edit.html',{'form':form})
@login_required			
def post_remove(request, pk):
	post = get_object_or_404(Post, pk = pk)
	post.delete()
	return redirect('post_list')

@login_required			
def post_draft_list(request):
	#Obtenemos la lista de posts que no están publicados filtrando los que no tengan fecha de publicación
	posts = Post.objects.filter(published_date__isnull = True).order_by('created_date')
	return render(request, 'blog/post_draft_list.html',{'posts':posts})
@login_required	
def post_publish(request, pk):
	post = get_object_or_404(Post, pk = pk)
	post.publish()
	return redirect('post_detail_blog', pk = pk)

	
def add_comment_to_post(request, pk):
	post = get_object_or_404(Post,pk = pk)
	
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.post = post
			comment.save()
			return redirect('post_detail_blog', pk = post.pk)
	else:
		form = CommentForm()
		return render(request, 'blog/comment_edit.html',{'form':form})
		
@login_required			
def edit_comment_to_post(request, pk):
	comment = get_object_or_404(Comments, pk = pk)
	if request.method == "POST":
		form = CommentForm(request.POST,  instance = comment )
		if form.is_valid():
			comment = form.save(commit = False)
			#comment.post = post
			comment.approved_comment = False
			comment.save()
			return redirect('post_detail_blog', pk=comment.post.pk)
	else: 
		form = CommentForm(instance = comment)
		return render(request, 'blog/comment_edit.html', {'form':form})
@login_required			
def aprove_comment(request, pk):
	comment = get_object_or_404(Comments, pk = pk)
	comment.approved()
	return redirect('post_detail_blog', pk = comment.post.pk)

@login_required	
def remove_comment(request, pk):	
	comment = get_object_or_404(Comments, pk = pk)
	comment.delete()
	return redirect('post_detail_blog', pk = comment.post.pk)

#def loginM(request):
#	return render(request,'registration/login.html')
# def logout_view(request):
	# logout(request)
	# return redirect('blog/logout.html')