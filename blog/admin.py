from django.contrib import admin
from .models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'date_published',
    )

    search_fields = (
        'title',
        'content',
    )

    list_filter = (
        'category',
        'date_published',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

    search_fields = (
        'title',
    )


admin.site.register(Post)
admin.site.register(Category)
