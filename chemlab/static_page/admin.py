from django.contrib import admin

from .models import StaticPage


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'published', 'content')
        }),
        ('SEO', {
            'fields': ('meta_description',),
        }),
    )
    search_fields = ('name',)
    list_display = ('name', 'slug', 'published')
    list_editable = ('published',)
    prepopulated_fields = {"slug": ("name",)}
