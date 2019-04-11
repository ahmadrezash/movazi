import logging
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView ,FormView
from django.utils.text import slugify

from panel.forms.NewsForm import NewsForm
from panel.models.NewsModel import News
from panel.models.CategoryModels import Category
from django.db import models
from django.core.paginator import Paginator

def index(request):
    posts = News.objects.order_by('pub_date')[:3]
    t = TemplateResponse(request, 'home.html', {'posts':posts})
    t.render()
    return HttpResponse(t)

def all_news(request):
    article_list = News.objects.all().order_by('-pub_date')
    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    print('sdsdsfs')
    return render(request, 'ContentManage/NewsTable.html', {'posts': article_list,'content':"News"})


# create_article
def create_news(request):
    saved = False
    if request.method == "POST":
        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_news')
            # return render(request, 'test.html', {'a':'مقاله با موفقست ثبت شد' })
        # return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = NewsForm()
        return render(request, 'Forms/NewsForm.html', {'form': form})



def update_news(request,slug):
    saved = False
    tmp = News.objects.filter(slug=slug)[0]

    if request.method == "POST":
        form = NewsForm(data=request.POST, files=request.FILES,instance = tmp)
        if form.is_valid():
            a = form.save(commit=False )
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_news')
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = NewsForm(instance=tmp)
        return render(request, 'Forms/NewsForm.html', {'form': form})

def delete_news(request,slug):
    News.objects.filter(slug=slug)[0].delete()
    # print('resiiiiiid')
    return redirect('all_news')
    # return render(request, 'test.html', {'a': slug})
