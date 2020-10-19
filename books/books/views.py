from django.shortcuts import render, reverse
from .forms import RegistrationForm, AddBookForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponseBadRequest
from .forms import UpdateDp, AddProgress

import logging

logger = logging.getLogger('__name__')


def index_view(request):
    if request.method == 'GET':
        return render(request, template_name='books/index.html')


def register(request):
    if request.method == 'GET':
        logger.info('Get request to register page')
        form = RegistrationForm()
        return render(request, template_name='books/register.html', context={'form': form})
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully, Please log in now')
            return HttpResponseRedirect(redirect_to=reverse('login'))
        else:
            logger.info('User registered successfully')
            return HttpResponseRedirect(redirect_to=reverse('register'))


def profile(request):
    if request.user.is_authenticated:
        form = UpdateDp()
        return render(request, template_name='books/profile.html', context={'user': request.user, 'form': form})
    else:
        messages.warning(request, 'First login to view your profile')
        return HttpResponseRedirect(redirect_to=reverse('login'))


def add_book(request):
    if request.method == 'GET':
        logger.info('Get request to display Add book form')
        form = AddBookForm()
        return render(request, template_name='books/add_book.html', context={'form': form})
    elif request.method == 'POST':
        logger.info('Post method called to submit form')
        form = AddBookForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(redirect_to=reverse('profile'))
        else:
            logger.error("Error in form {}".format(form.errors))
            return HttpResponseRedirect(redirect_to=reverse('add_book'))


def upload_dp(request):

    if request.method == "POST":
        if request.user.is_authenticated:
            form = UpdateDp(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                logger.info("Profile picture updated")
                messages.success(request, 'Profile picture updated')
                return HttpResponseRedirect(redirect_to=reverse('profile'))
            else:
                logger.error("for is not valid {}".format(form.errors))
                messages.error(request, 'Invalid form submission')
                return HttpResponseRedirect(redirect_to=reverse('profile'))
        else:
            logger.error("user not authenticated")
            return HttpResponseRedirect(redirect_to=reverse('login'))
    else:
        logger.error("Method {} not allowed in upload_dp api".format(request.method))
        return HttpResponseBadRequest


def add_progress(request):

    if request.method == 'GET':
        form = AddProgress()
        return render(request, template_name="books/add_progress.html", context={'form': form})
    elif request.method == 'POST':
        form = AddProgress(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            logger.info("Progress Created")
            messages.success(request, 'Progress Created')
            return HttpResponseRedirect(redirect_to=reverse('profile'))