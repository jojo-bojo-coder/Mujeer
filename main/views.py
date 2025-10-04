from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    context = {
        'page_title': _("Mujeer Hotel Management and Operations Company"),
        # We'll add more translated variables as needed
    }
    return render(request, 'main/index.html', context)

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            request.session['django_language'] = language
            activate(language)
    return redirect('index')
