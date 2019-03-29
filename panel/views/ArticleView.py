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

from panel.forms.ArticleForm import ArticleForm
from panel.models.ArticleModels import Article
from panel.models.CategoryModels import Category
from django.db import models
from django.core.paginator import Paginator

def index(request):
    posts = Article.objects.order_by('pub_date')[:3]
    t = TemplateResponse(request, 'home.html', {'posts':posts})
    t.render()
    return HttpResponse(t)

def all_article(request):
    article_list = Article.objects.all().order_by('-pub_date')
    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    article_list = paginator.get_page(page)
    # print('sdsdsfs')
    return render(request, 'ContentManage/ArticleTable.html', {'posts': article_list,'content':"article"})


# create_article
def create_article(request):
    saved = False
    if request.method == "POST":
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('article_all')
            # return render(request, 'test.html', {'a':'مقاله با موفقست ثبت شد' })
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = ArticleForm()
        return render(request, 'Forms/ArticleForm.html', {'form': form})



def update_article(request,slug):
    saved = False
    tmp = Article.objects.filter(slug=slug)[0]

    if request.method == "POST":
        form = ArticleForm(data=request.POST, files=request.FILES,instance = tmp)
        if form.is_valid():
            a = form.save(commit=False )
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('article_all')
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = ArticleForm(instance=tmp)
        return render(request, 'Forms/ArticleForm.html', {'form': form})

def delete_article(request,slug):
    Article.objects.filter(slug=slug)[0].delete()
    # print('resiiiiiid')
    return redirect('article_all')
    # return render(request, 'test.html', {'a': slug})
