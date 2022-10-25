
def add_context(request):
    return {
        'page_path': request.path,
        'user': request.user if request.user.is_authenticated else None
    }
