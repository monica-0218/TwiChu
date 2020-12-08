from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail_disp', 'tag_list')
    list_display_links = ('id', 'title')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def thumbnail_disp(self, obj):
        return mark_safe("<img src='{}'  width='100' height='60' />".format(obj.thumbnail.url))

admin.site.register(Post, PostAdmin)