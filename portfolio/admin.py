from django.contrib import admin
from adminsortable2.admin import SortableAdminBase, SortableAdminMixin, SortableInlineAdminMixin

from .models import Series, Photo

class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Photo
    extra = 0
    fields = ("image", "title_es", "title_en", "year", "location", "order")
    readonly_fields = ()
    ordering = ("order",)

@admin.register(Series)
class SeriesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title_es", "slug", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("title_es",)}
    inlines = [PhotoInline]
    ordering = ("order",)

@admin.register(Photo)
class PhotoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("series", "id", "order", "year", "location")
    list_filter = ("series",)
    search_fields = ("title_es", "title_en", "location", "year")
    ordering = ("series", "order")
