from .models import StaticPage


def add_static_pages_to_context(request):
    return {
        'static_pages': StaticPage.objects.filter(published=True),
        'stripped_path': request.path_info.strip('/'),
    }
