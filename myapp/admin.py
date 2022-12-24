from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}

admin.site.register(Service)
admin.site.register(SubPortfolio)
admin.site.register(Testimonial)
admin.site.register(Work_Summary)
admin.site.register(UserProfile)
admin.site.register(Category)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','subject', 'created_on')
    search_fields = ['subject', 'body']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'name','post', 'content', 'email', 'publish', 'status')
    list_filter= ('status', 'publish')
    search_fields = ['name', 'email']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'body']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title', )}




#Other ways of styling the admin area
# class postAdmin(admin.Model):
#     list_display = ['id', 'user' ]
#     ordering = ['d']
#     admin.site.register(Post,postAdmin)