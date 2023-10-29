from django.contrib import admin
from .models import Catagory,Post
# Register your models here.

#custom Categoryadmin Dashboard
class CatagoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','description','add_date')
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    search_fields=('title',)
    list_display=('title','post_id','url')
    list_filter = ('title',)
    list_per_page=10
    class Media:
        js=("https://cdn.tiny.cloud/1/qn2azvfald1vuf09eu8cw31k8fntgj2tg9ruqizpj0tlu5od/tinymce/6/tinymce.min.js",'js/static.js',)
# registered Models
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Post, PostAdmin)