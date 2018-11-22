from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
	path('', views.post_list, name = 'post_list'),
	path('listOrdered/', views.post_list_new, name = 'post_list_new'),
	#URL que dirige a Django hacia una vista llamada postDetail q mostrará una entrada del blog completa, pk es una clave númerica que se generará en cada post 
	path('post/<int:pk>', views.post_detail_blog, name = 'post_detail_blog'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
	path('post/<int:pk>/remove/',views.post_remove, name = 'post_remove'),
	url(r'^drafts/$',views.post_draft_list, name = 'post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	# url(r'^account/logout/',views.logout_view, name = 'logout_view'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name = 'add_comment_to_post'),
	url(r'^comment/(?P<pk>\d+)/edit/$',views.edit_comment_to_post, name = 'edit_comment_to_post'),
	url(r'^comment/(?P<pk>\d+)/aprove/$', views.aprove_comment, name = 'aprove_comment'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.remove_comment, name = 'remove_comment' ),
]

#path('', views.post_draft_list, name = 'post_draft_list')