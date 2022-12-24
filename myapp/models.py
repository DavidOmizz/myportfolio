from django.db import models
from django.contrib.auth.models import  User
from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)



class Category(models.Model):
    cat_name = models.CharField(max_length = 200)
    desription = models.TextField()

    def __str__(self):
        return self.cat_name

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    age = models.IntegerField()
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user


class About(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=300)
    profile = models.CharField(max_length=300)
    email = models.EmailField()
    phone_no = models.IntegerField()
    created_on = models.DateTimeField(default=timezone.now)
    # body = HTMLField()
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=300)
    

    def __str__(self):
        return self.name

class Service(models.Model):
    sub_service = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    created_on = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    slug = models.SlugField(max_length=300)
    

    def __str__(self):
        return self.body


# PORTFOLIO SECTION
class Portfolio(models.Model):
    image = models.ImageField()
    images = models.ImageField()
    imagess = models.ImageField()
    title = models.CharField(max_length=300)
    # body = models.TextField()
    body = RichTextUploadingField()
    created_on = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Category')
    slug = models.SlugField(max_length=300)
    client = models.TextField()
    project_url = models.CharField(max_length=300)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
class SubPortfolio(models.Model):
    sub_portfolio = models.CharField(max_length=300)

    def __str__(self):
        return self.sub_portfolio


class Blog(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=300, unique=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Category')
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_post')
    body = RichTextUploadingField()
    created_on = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=300, unique= True)
    duration = models.CharField(max_length=300)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    image = models.ImageField()
    client_name = models.CharField(max_length=300)
    client_comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.client_name

class Work_Summary(models.Model):
    title = models.CharField(max_length=300)
    no_of_jobs = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=3000)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=500)
    email = models.EmailField()
    content = models.TextField()
    status = models.BooleanField(default=True)
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment by ( self.name)'
    

