from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *

from django.db.models import Q

from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from collections import OrderedDict



def register(request):
    if request.method == "POST":
        u_form = UserRegisterForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('profile')
    else:
        u_form = UserRegisterForm()
    return render(request, 'news_app/register.html', {'u_form': u_form})


@login_required
def profile(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(
            request.POST, instance=request.user.userprofile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Profile successfully Updated!')
            return redirect('home')
    else:
        try:
            p_form = ProfileUpdateForm(instance=request.user.userprofile)
        except:
            p_form = ProfileUpdateForm()
    context = {'p_form': p_form}
    return render(request, 'news_app/profile.html', context)




@login_required
def home(request):
    news_list = []
    #To remove duplicate news and also to maintain the order of the news (latest),
    #sets remove duplicate but changes order, so import ordereddict and use this method
    news = OrderedDict.fromkeys(News.objects.filter(
        Q(publisher__in=request.user.userprofile.publisher.all()) & Q(category__in=request.user.userprofile.category.all())).order_by('-id'))
    return render(request, 'news_app/news.html', {'newslist': news})


class newsDetailView(generic.DetailView):
    model = News







class catDetailView(generic.DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(catDetailView, self).get_context_data(**kwargs)
        news =  OrderedDict.fromkeys(News.objects.filter(category=self.kwargs['pk']).order_by('-id'))
        context['newslist'] = news
        return context


class pubDetailView(generic.DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):

        context = super(pubDetailView, self).get_context_data(**kwargs)
        news =  OrderedDict.fromkeys(News.objects.filter(publisher=self.kwargs['pk']).order_by('-id'))
        context['newslist'] = news
        return context


@login_required
def add(request):
    if request.method == "POST":
        news_form = NewsCreationForm(request.POST, request.FILES)
        if news_form.is_valid():
            news_form.save()
            publisher = news_form.cleaned_data.get('publisher')
            messages.success(request, f'News Added from {publisher}!')
            return redirect('home')
    else:
        if request.user.userprofile.is_publisher:
            news_form = NewsCreationForm()
        else:
            raise Http404("You are not authorised to view this page")
    return render(request, 'news_app/add.html', {'news_form': news_form})
