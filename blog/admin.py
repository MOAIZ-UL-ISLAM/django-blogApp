from django.contrib import admin
from .models import Catagory,Post
# Register your models here.

#custom Categoryadmin Dashboard
class CatagoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','description','add_date')
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','cat','post_id')


# registered Models
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Post, PostAdmin)