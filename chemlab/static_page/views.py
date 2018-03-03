from django.views.generic.detail import DetailView

from .models import StaticPage


class StaticPageView(DetailView):
    model = StaticPage
    template_name = 'static_page/static_page.html'
    context_object_name = 'page'
