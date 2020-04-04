from django.shortcuts import render, get_object_or_404, redirect
from .forms import DocumentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Document
from django.conf import settings
import os

def notify1(request):
    return render(request,'crisis/notify1.html')

def notify2(request):
    return render(request,'crisis/notify2.html')

def image3(request):
    v = "result0003.jpg"
    a = "1"
    return render(request,'crisis/mlmodel.html',{'img':v,'b':a})

def image2(request):
    v = "result0007.jpg"
    a = "0"
    return render(request,'crisis/mlmodel.html',{'img':v,'b':a})

def special(request,pk):
    obj = get_object_or_404(Document,pk=pk)
    return render(request,'crisis/special.html',{'source':obj})

def index(request):
    obj = Document.objects.all()
    return render(request,'crisis/index.html',{'obj':obj})

def register(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.cleaned_data.get("document")
            name = form.cleaned_data.get("name")
            newobj = Document(document=profile,name=name,description="0")
            newobj.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'crisis/registration.html', {
        'form': form
    })
