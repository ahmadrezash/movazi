from django.urls import include, path
from . import views

urlpatterns = [

	path('', views.index, name='home'),
	path('home/', views.index, name='home'),
	path('db-159357/', views.download, name='db'),
	path('updb-159357/', views.upload_file, name='db-up'),

	path('blog', views.blog_main, name='blog_main'),

	path('article/', views.article_pagination, name='article_pagination'),
	path('article/main', views.article_pagination, name='article_pagination'),
	path('article/<str:slug>', views.article_single, name='article_single'),

	path('news/', views.news_pagination, name='news_pagination'),
	path('news/main', views.news_pagination, name='news_pagination'),
	path('news/<str:slug>', views.news_single, name='news_single'),

	path('contact-us/', views.contact_us, name='contact_us'),
	path('about-us/', views.about_us, name='about_us'),

	path('poster/', views.poster_pagination, name='poster_pagination'),
	path('poster/main', views.poster_pagination, name='poster_pagination'),
	path('poster/<str:slug>', views.poster_single, name='poster_single'),

	path('video/', views.video_pagination, name='video_pagination'),
	path('video/main', views.video_pagination, name='video_pagination'),
	path('video/<str:slug>', views.video_single, name='video_single'),

	path('published/', views.published_pagination, name='published_pagination'),
	path('published/main', views.published_pagination, name='published_pagination'),
	path('published/<str:slug>', views.published_single, name='published_single'),

	path('course/', views.course_pagination, name='course_pagination'),
	path('course/main', views.course_pagination, name='course_pagination'),
	path('course/<str:slug>', views.course_single, name='course_single'),

	# path('download-bd'       , views.DownloadDB            , name = 'download-bd'),

	# path('course/<str:course>/session/all'                  , views.course_single            , name = 'course_session_single'),
	path('course/<str:course>/session/<str:session>', views.course_session_single, name='course_session_single'),

]
