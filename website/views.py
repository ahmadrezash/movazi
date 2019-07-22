# For HTML
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Models
from panel.models.ArticleModels import Article
from panel.models.Published.PublishedModel import Published
from panel.models.NewsModel import News
from panel.models.MultiMedia.PosterModel import Poster
from panel.models.MultiMedia.VideoModel import Video
from panel.models.Courses.CourseModel import Course
from panel.models.Courses.CourseSessionModel import CourseSession
from panel.models.CategoryModels import Category

# Pagination
from django.core.paginator import Paginator

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse  # Add this

from django.core.mail import send_mail

from website.form import ContactForm


def index(request):
	news = News.objects.order_by('-pub_date')[:4]
	video = Video.objects.order_by('-pub_date')[:5]
	poster = Poster.objects.order_by('-pub_date')[:4]
	t = TemplateResponse(request, 'home.html', {'news': news, 'posters': poster, 'videos': video})
	t.render()
	return HttpResponse(t)


# Single Pages

# def contact_us(request):
#     t = TemplateResponse(request, 'contact_us.html')
#     t.render()
#     return HttpResponse(t)


def contact_us(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# send email code goes here
			sender_name = form.cleaned_data['name']
			sender_email = form.cleaned_data['email']

			message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
			send_mail('New Enquiry', message, sender_email, ['ahmad.sharif.abc@gmail.com'], fail_silently=False)
			return render(request, 'home.html')
	else:
		form = ContactForm()

	return render(request, 'contact_us.html', {'form': form})


def about_us(request):
	t = TemplateResponse(request, 'about_us.html')
	t.render()
	return HttpResponse(t)


def blog_main(request):
	t = TemplateResponse(request, 'blog/index.html', {})
	t.render()
	return HttpResponse(t)


# Model Pages


## Articles

def article_pagination(request):
	article_list = Article.objects.all()
	paginator = Paginator(article_list, 4)
	page = request.GET.get('page')
	article_list = paginator.get_page(page)
	cats = Category.objects.all()

	return render(request, 'blog/article_all.html', {'posts': article_list, 'cats': cats})


def article_single(request, slug):
	cats = Category.objects.all()
	article = Article.objects.filter(slug=slug).get()
	return render(request, 'blog/article_single.html', {'post': article, 'cats': cats})


def news_pagination(request):
	article_list = News.objects.all()
	paginator = Paginator(article_list, 4)
	page = request.GET.get('page')
	article_list = paginator.get_page(page)
	cats = Category.objects.all()
	return render(request, 'blog/news_all.html', {'posts': article_list, 'cats': cats})


def news_single(request, slug):
	cats = Category.objects.all()
	article = News.objects.filter(slug=slug).get()
	return render(request, 'blog/news_single.html', {'post': article, 'cats': cats})


def poster_pagination(request):
	article_list = Poster.objects.all()
	paginator = Paginator(article_list, 4)
	page = request.GET.get('page')
	article_list = paginator.get_page(page)
	cats = Category.objects.all()

	return render(request, 'blog/poster_all.html', {'posts': article_list, 'cats': cats})


def poster_single(request, slug):
	cats = Category.objects.all()
	article = Poster.objects.filter(slug=slug).get()
	return render(request, 'blog/poster_single.html', {'post': article, 'cats': cats})


def video_pagination(request):
	article_list = Video.objects.all()
	paginator = Paginator(article_list, 4)
	page = request.GET.get('page')
	article_list = paginator.get_page(page)
	cats = Category.objects.all()

	return render(request, 'blog/video_all.html', {'posts': article_list, 'cats': cats})


def video_single(request, slug):
	cats = Category.objects.all()
	article = Video.objects.filter(slug=slug).get()
	return render(request, 'blog/video_single.html', {'post': article, 'cats': cats})


# return render(request, 'test.html', {'a': article})


def published_pagination(request):
	published_list = Published.objects.all()
	paginator = Paginator(published_list, 4)
	page = request.GET.get('page')
	published_list = paginator.get_page(page)
	cats = Category.objects.all()

	return render(request, 'blog/published_all.html', {'posts': published_list, 'cats': cats})


def published_single(request, slug):
	cats = Category.objects.all()
	published = Published.objects.filter(slug=slug).get()
	return render(request, 'blog/published_single.html', {'post': published, 'cats': cats})


def course_pagination(request):
	course_list = Course.objects.all()
	paginator = Paginator(course_list, 4)
	page = request.GET.get('page')
	course_list = paginator.get_page(page)
	cats = Category.objects.all()

	return render(request, 'blog/course_all.html', {'posts': course_list, 'cats': cats})


def course_single(request, slug):
	cats = Category.objects.all()
	course = Course.objects.filter(slug=slug).get()
	session = CourseSession.objects.filter(course=course)

	return render(request, 'blog/course_single.html', {'post': course, 'cats': cats, "sessions": session})


def course_session_single(request, course, session):
	cats = Category.objects.all()
	course = CourseSession.objects.filter(slug=session).get()
	return render(request, 'blog/course_session_single.html', {'post': course, 'cats': cats})


import os
from django.conf import settings
from django.http import HttpResponse, Http404


def download(request, path='db.sqlite3'):
	file_path = os.path.join(settings.MEDIA_ROOT, path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404


# views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import UploadFileForm


# Imaginary function to handle an uploaded file.
def handle_uploaded_file(f):
	with open(os.path.join(settings.MEDIA_ROOT, 'db.sqlite3'), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)


from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def upload_file(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return render(request, 'upload.html', {
			'uploaded_file_url': uploaded_file_url
		})
	return render(request, 'upload.html')
