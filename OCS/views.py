from django.shortcuts import render, get_object_or_404, HttpResponse, Http404

def index(request):
    return render(request,'index.html')