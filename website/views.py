from django.shortcuts import render


# Create your views here.
def index(request):
    # return render(request, 'base.html')
    return render(request, 'website/index.html')


