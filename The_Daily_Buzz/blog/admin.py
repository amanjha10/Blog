from django.contrib import admin
from .models import Category ,Post

# Register your models here.

# For configuration of Category

class Categoryadmin(admin.ModelAdmin):
    list_display=('image_tag','title','description','add_date','url')
    search_fields=('title',)

class Postadmin(admin.ModelAdmin):
    list_display=('images','title','url')
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=50

    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)


admin.site.register(Category ,Categoryadmin)
admin.site.register(Post, Postadmin)
