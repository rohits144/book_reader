from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect
from django.core.exceptions import ValidationError
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
            return HttpResponseRedirect(redirect_to=reverse('login'))
        else:
            logger.info('User registered successfully')
            return HttpResponseRedirect(redirect_to=reverse('register'))


def profile(request):
    if request.user.is_authenticated:
        return render(request, template_name='books/profile.html', context={'user': request.user})
    else:
        return HttpResponseRedirect(redirect_to=reverse('login'))
