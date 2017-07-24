"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import GoodModel
from app.models import ReviewModel
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect

success = False
def home(request):
    """Renders the home page."""
    success = False
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            messages.info(request, 'Новые отзывы!')
            form.save()
            success = True
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'), locals())
    goods=GoodModel.objects.all()
    reviews = ReviewModel.objects.filter(validated=True)
    return render(request, 'app/index.html', locals())

