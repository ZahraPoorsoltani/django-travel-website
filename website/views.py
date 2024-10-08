from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from website.forms import ContactForm,NewsLetterForm
from django.contrib import messages
from website.models import Contact
from django.template import Context, loader


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.name = 'anonymous' 
            new_contact.save()
            
            messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully!')
        else:
            messages.add_message(request,messages.ERROR,'please check your input format')


    form = ContactForm()
    return render(request,'contact.html',{'form':form})

def news_letter(request):
    if request.method == 'POST':
        form = NewsLetterForm(data = request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')



def handler404(request, exception, template_name="404.html"):
    return render(request,'404.html',status=404)

def handler500(request,*args, **argv):
    return render(request,'500.html',status=500)
