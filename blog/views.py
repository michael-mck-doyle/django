from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')

# HttpResponse("This is my blog")

# Create your views here.
