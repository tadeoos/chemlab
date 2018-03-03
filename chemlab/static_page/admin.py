from django.contrib import admin

from .models import StaticPage


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'content', 'published')
        }),
        ('SEO', {
            # 'classes': ('collapse',),
            'fields': ('meta_description',),
        }),
    )
    search_fields = ('name',)
    list_display = ('name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}
