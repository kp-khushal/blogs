from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse 


# Create your models here.
STATUS = (
    (0, "Drafts"),
    (1, "Publish")
)



class Post(models.Model):
    id = models.AutoField(primary_key=True) 
    slug = models.SlugField(max_length = 250)
    title = models.CharField(max_length = 200)
    meta_description = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    title_tag = models.CharField(max_length = 200)
    content = RichTextField(blank = True,null = True)
    #content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)
    
    def __str__(self):
        return self.title
  
    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))

    