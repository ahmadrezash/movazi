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
from django.core.paginator import Paginator

from panel.forms.MultiMediaForm.PosterForm import PosterForm
from panel.models.MultiMedia.PosterModel import Poster
from panel.forms.MultiMediaForm.VideoForm import VideoForm
from panel.models.MultiMedia.VideoModel import Video
from panel.models.CategoryModels import Category
from django.db import models

# def poster_main(request):
#     posts = PosterForm.objects.order_by('pub_date')[:3]
#     t = TemplateResponse(request, 'home.html', {'posts':posts})
#     t.render()
#     return HttpResponse(t)

def all_poster(request):
    poster_list = Poster.objects.all().order_by('-pub_date')
    paginator = Paginator(poster_list, 10)
    page = request.GET.get('page')
    poster_list = paginator.get_page(page)
    # print('sdsdsfs')
    return render(request, 'ContentManage/PosterTable.html', {'posts': poster_list})


# create_Poster
def create_poster(request):
    saved = False
    if request.method == "POST":
        form = PosterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_poster')
            # return render(request, 'test.html', {'a':'مقاله با موفقست ثبت شد' })
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = PosterForm()
        return render(request, 'Forms/PosterForm.html', {'form': form})

def update_poster(request,slug):
    saved = False
    tmp = Poster.objects.filter(slug=slug)[0]

    if request.method == "POST":
        form = PosterForm(data=request.POST, files=request.FILES,instance = tmp)
        if form.is_valid():
            a = form.save(commit=False )
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_poster')
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = PosterForm(instance=tmp)
        return render(request, 'Forms/PosterForm.html', {'form': form})

def delete_poster(request,slug):
    Poster.objects.filter(slug=slug)[0].delete()
    # print('resiiiiiid')
    return redirect('all_poster')
    # return render(request, 'test.html', {'a': slug})






def all_video(request):
    poster_list = Video.objects.all().order_by('-pub_date')
    paginator = Paginator(poster_list, 10)
    page = request.GET.get('page')
    poster_list = paginator.get_page(page)
    return render(request, 'ContentManage/VideoTable.html', {'posts': poster_list})


# create_Poster
def create_video(request):
    saved = False
    if request.method == "POST":
        form = VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_video')
            # return render(request, 'test.html', {'a':'مقاله با موفقست ثبت شد' })
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = VideoForm()
        return render(request, 'Forms/VideoForm.html', {'form': form})

def update_video(request,slug):
    saved = False
    tmp = Video.objects.filter(slug=slug)[0]

    if request.method == "POST":
        form = VideoForm(data=request.POST, files=request.FILES,instance = tmp)
        if form.is_valid():
            a = form.save(commit=False )
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_video')
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = VideoForm(instance=tmp)
        return render(request, 'Forms/VideoForm.html', {'form': form})

def delete_video(request,slug):
    Video.objects.filter(slug=slug)[0].delete()
    return redirect('all_video')







def video_main(request,CreateView):
    posts = VideoForm.objects.order_by('pub_date')[:3]
    t = TemplateResponse(request, 'home.html', {'posts':posts})
    t.render()
    return HttpResponse(t)

# def create_video(request):
#     saved = False
#     if request.method == "POST":
#         form = VideoForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             a = form.save(commit=False)
#             a.author = request.user
#             a.category = Category.objects.all()[0]
#             a.save()
#             return render(request, 'test.html', {'a':'مقاله با موفقست ثبت شد' })
#         return render(request, 'test.html', {'a': form.errors})
#     else:
#         form = VideoForm()
#         return render(request, 'Forms/VideoForm.html', {'form': form})

# def update_Poster(request,title):
   



