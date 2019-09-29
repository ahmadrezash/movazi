import logging
from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.contrib.auth.forms import UserCreationForm

from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from panel.forms import ArticleForm
from panel.models.ArticleModels import Article


def panel(request):
	# posts = ['ahmad']*10
	# t = TemplateResponse(request, 'a.html', {'posts':posts})
	t = TemplateResponse(request, 'panel_start.html', {'a': 'asasa'})

	t.render()
	return HttpResponse(t)


def aa(request):
	# posts = ['ahmad']*10
	# t = TemplateResponse(request, 'a.html', {'posts':posts})
	t = TemplateResponse(request, 'aa.html')

	t.render()
	return HttpResponse(t)


class SignUp(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'
