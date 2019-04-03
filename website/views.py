from django.shortcuts                        import render
from django.http                             import HttpResponse
from django.template.response                import TemplateResponse
from panel.models.ArticleModels              import Article
from panel.models.Published.PublishedModel   import Published
from panel.models.NewsModel                  import News
from panel.models.MultiMedia.PosterModel     import Poster
from panel.models.MultiMedia.VideoModel      import Video
from panel.models.Courses.CourseModel        import Course
from panel.models.Courses.CourseSessionModel import CourseSession


from panel.models.CategoryModels import Category
from django.core.paginator import Paginator
from django.shortcuts import render

def index(request):
    news = News.objects.order_by('-pub_date')[:4]
    poster = Poster.objects.order_by('-pub_date')[:4]
    t = TemplateResponse(request, 'home.html', {'news':news,'posters':poster})
    # t = TemplateResponse(request, 'test.html', {'a':poster})
    t.render()
    return HttpResponse(t)

def contact_us(request):
    t = TemplateResponse(request, 'contact_us.html')
    t.render()
    return HttpResponse(t)

def about_us(request):
    t = TemplateResponse(request, 'about_us.html')
    t.render()
    return HttpResponse(t)
    
def blog_main(request):
    t = TemplateResponse(request, 'blog/index.html', {})
    t.render()
    return HttpResponse(t)


def article_pagination(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 4)
    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    cats = Category.objects.all()

    return render(request, 'blog/article_all.html', {'posts': article_list,'cats':cats})

def article_single(request,slug):
    cats = Category.objects.all()
    article = Article.objects.filter(slug=slug).get()
    return render(request, 'blog/article_single.html', {'post': article,'cats':cats})


def news_pagination(request):
    article_list =News.objects.all()
    paginator = Paginator(article_list, 4)
    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    cats = Category.objects.all()
    return render(request, 'blog/news_all.html', {'posts': article_list,'cats':cats})

def news_single(request,slug):
    cats = Category.objects.all()
    article =News.objects.filter(slug=slug).get()
    return render(request, 'blog/news_single.html', {'post': article,'cats':cats})

def poster_pagination(request):
    article_list = Poster.objects.all()
    paginator = Paginator(article_list, 4)
    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    cats = Category.objects.all()

    return render(request, 'blog/poster_all.html', {'posts': article_list,'cats':cats})

def poster_single(request,slug):
    cats = Category.objects.all()
    article = Poster.objects.filter(slug=slug).get()
    return render(request, 'blog/poster_single.html', {'post': article,'cats':cats})


def video_pagination(request):
    article_list = Video.objects.all()
    paginator = Paginator(article_list, 4)
    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    cats = Category.objects.all()

    return render(request, 'blog/video_all.html', {'posts': article_list,'cats':cats})

def video_single(request,slug):
    cats = Category.objects.all()
    article = Video.objects.filter(slug=slug).get()
    return render(request, 'blog/video_single.html', {'post': article,'cats':cats})
    # return render(request, 'test.html', {'a': article})


def published_pagination(request):
    published_list = Published.objects.all()
    paginator = Paginator(published_list, 4)
    page = request.GET.get('page')
    published_list = paginator.get_page(page)
    cats = Category.objects.all()

    return render(request, 'blog/published_all.html', {'posts': published_list,'cats':cats})

def published_single(request,slug):
    cats = Category.objects.all()
    published = Published.objects.filter(slug=slug).get()
    return render(request, 'blog/published_single.html', {'post': published,'cats':cats})



def course_pagination(request):
    course_list = Course.objects.all()
    paginator = Paginator(course_list, 4)
    page = request.GET.get('page')
    course_list = paginator.get_page(page)
    cats = Category.objects.all()

    return render(request, 'blog/course_all.html', {'posts': course_list,'cats':cats})

def course_single(request,slug):
    cats    = Category.objects.all()
    course  = Course.objects.filter(slug=slug).get()
    session = CourseSession.objects.filter(course=course)

    return render(request, 'blog/course_single.html', {'post': course,'cats':cats,"sessions":session})

def course_session_single(request,course,session):
    cats = Category.objects.all()
    course = CourseSession.objects.filter(slug=session).get()
    return render(request, 'blog/course_session_single.html', {'post': course,'cats':cats})
