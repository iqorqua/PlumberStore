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

def home(request):
    """Renders the home page."""
    form_review = ReviewForm
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)

        if form.is_valid():
           form.save() 

    assert isinstance(request, HttpRequest)
    goods=GoodModel.objects.all()
    return render(request, 'app/index.html', locals())

