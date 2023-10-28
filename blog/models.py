from django.db import models
from django.utils.html import format_html
# Create your models here.


class Catagory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(blank=True, max_length=100)
    image = models.ImageField(upload_to='catalog/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}"  alt="image" styles="width:20px;heigth:20px;border-radius:50%" />'.format(self.image))

    def __str__(self):
        return self.title
    

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

    

    def __str__(self):
        return self.title