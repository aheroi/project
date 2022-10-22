from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'website/index.html')


def get_page_path(request):
    return {
        'page_path': request.path,
    }
