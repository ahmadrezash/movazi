import logging
from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView ,FormView
from django.utils.text import slugify

from panel.forms.PublishedForm import PublishedForm
from panel.models.Published.PublishedModel import Published
from panel.models.CategoryModels import Category
from django.db import models
from django.core.paginator import Paginator

def index(request):
    posts = Published.objects.order_by('pub_date')[:3]
    t = TemplateResponse(request, 'home.html', {'posts':posts})
    t.render()
    return HttpResponse(t)

def all_published(request):
    published_list = Published.objects.all().order_by('-pub_date')
    paginator = Paginator(published_list, 10)
    page = request.GET.get('page')
    published_list = paginator.get_page(page)
    # print('sdsdsfs')
    return render(request, 'ContentManage/PublishedTable.html', {'posts': published_list,'content':"Published"})


# create_published
def create_published(request):
    saved = False
    if request.method == "POST":
        form = PublishedForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_published')
        return render(request, 'test.html', {'a': form.errors})
    else:
        form = PublishedForm()
        return render(request, 'Forms/PublishedForm.html', {'form': form})



def update_published(request,slug):
    saved = False
    tmp = Published.objects.filter(slug=slug)[0]

    if request.method == "POST":
        form = PublishedForm(data=request.POST, files=request.FILES,instance = tmp)
        if form.is_valid():
            a = form.save(commit=False )
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_published')
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = PublishedForm(instance=tmp)
        return render(request, 'Forms/PublishedForm.html', {'form': form})

def delete_published(request,slug):
    Published.objects.filter(slug=slug)[0].delete()
    # print('resiiiiiid')
    return redirect('all_published')
    # return render(request, 'test.html', {'a': slug})
