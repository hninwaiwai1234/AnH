from django.shortcuts import render
from .models import Page
# Create your views here.
def home(request):
	pages = Page.objects.all()
	return render(request,'shop/home.html',{'pages':pages})
