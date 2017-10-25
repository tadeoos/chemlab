from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe


class MyWidget(Widget):
    template_name = 'survey/tag_input_widget.html'

    def get_context(self, name, value, attrs=None):
        return {
            'name': name,
            'api': self.attrs['api']
        }

    def render(self, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)