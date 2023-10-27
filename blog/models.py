from django.db import models

# Create your models here.
class Catagory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url =models.CharField(blank=True,max_length=100)
    image = models.ImageField(upload_to='catalog/')
    add_date = models.DateTimeField(auto_now_add=True,null=True)


class Post(models.Model):
    post_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url =models.CharField(max_length=100)
    cat = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')