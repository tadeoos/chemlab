from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


class StaticPage(models.Model):
    """Model implementing static page functionality."""
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=140, unique=True, verbose_name=_("Slug"))
    content = models.TextField(
        verbose_name=_("Content"),
        help_text=mark_safe(_("You can use <a href='http://commonmark.org/help/'>MarkDown</a> formatting")))
    published = models.BooleanField(default=False, verbose_name=_("Published"))
    meta_description = models.TextField(
        verbose_name=_("SEO: Meta description"),
        blank=True,
        max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('static-page', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _("Static Page")
        verbose_name_plural = _("Static Pages")
