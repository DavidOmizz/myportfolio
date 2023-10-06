# from django.views.generic import DetailView
# from multiprocessing import context
# from re import template
# from turtle import title
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .forms import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import  User

from django.core.mail import send_mail,BadHeaderError


# from .forms import CommentForm, ContactForm
# from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
    about = About.objects.all()
    blog = Blog.objects.filter(status='1').order_by('-created_on')[:3]
    portfolio = Portfolio.objects.all()
    sub_portfolio = SubPortfolio.objects.all()
    testimonials = Testimonial.objects.all()
    template_name = 'index.html'
    if request.method == 'POST':
        contact = ContactForm(data=request.POST)
        if contact.is_valid():
            email = contact.cleaned_data['email']
            name = contact.cleaned_data['name']
            subject = contact.cleaned_data['subject']
            message = contact.cleaned_data['message']
            contact.save()
            try:
                send_mail(
                    subject,
                    message,
                    email,
                    ["davidomisakin4good@gmail.com"],
                    fail_silently=False,
                )
            except BadHeaderError as e:
                print(f"BadHeaderError: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
        messages.success(request,'Message sent succesffully')
    else:
        contact = ContactForm()
    # from django.contrib.auth.models import User
    # print(User.objects.all())
    # usr = User.objects.get(username='david')
    # usr.set_password('David@2001')
    # usr.save()
    user  = User.objects.all()
    print(user)
    return render (request, template_name, {'about': about,'blog':blog,'portfolio': portfolio, 'sub_portfolio':sub_portfolio, 'testimonials':testimonials, 'cform':contact} )

def blog_single(request, slug):
    blog = get_object_or_404(Blog, slug=slug,)
    blogside = Blog.objects.all()[:4]
    comments = blog.comments.filter(status=True)
    user_comment = None
    if request.method =='POST':
        comment = CommentForm(data=request.POST)
        if comment.is_valid():
             # Create Comment object but don't save to database yet
            user_comment = comment.save(commit=False)
            # Assign the current post to the comment
            user_comment.post = blog
            # Save the comment to the database
            user_comment.save()
            messages.success(request,'Comment added succesffully')
            return HttpResponseRedirect('/' + blog.slug)
    else:
        comment = CommentForm()

    return render(request, 'blog-single.html', {'blog':blog, 'blogside':blogside, 'comment':comment, 'comments':comments, 'user_comment':user_comment} )

def blog_list(request):
    template_name = 'blog-list.html'
    blogsides = Blog.objects.all()[:4]
    bloglist = Blog.objects.all()
    
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     data = Blog.objects.filter(title__icontains= q)
    # else :
    #     data = Blog.objects.all() 

    query = request.GET.get('q')
    if query:
        bloglist = Blog.objects.filter(Q(title__icontains = query) | Q(body__icontains = query)).order_by('-created_on')
    else:
        bloglist = Blog.objects.all()

    if not bloglist:
        messages.warning(request, 'No content found!')
    
    return render(request, template_name,{'bloglist':bloglist,'blogsides':blogsides})

# class BlogSearchView(ListView):
    model = Blog
    template_name = "blog-list.html"
    context_object_name = 'bloglist'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            context_object_name = Blog.objects.filter(Q(title__icontains = query) | Q(body__icontains = query))
            return context_object_name
        
        else:
            context_object_name = Blog.objects.all()
        
        if not context_object_name:
            return HttpResponse('No cotent found')



def portfolio_single(request, slug):
    psingle = get_object_or_404(Portfolio, slug=slug)
    return render(request, 'portfolio-details.html', {'psingle': psingle} )



# def register(request):
#     # register_form = RegForm.objects.all()
#     if request.method == 'POST':
#         register_form = RegForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             return redirect('login')
#     else:
#         register_form = RegForm()
#     return render(request, 'register.html', {'reg': register_form})
def register(request):
    # register_form = RegForm.objects.all()
    if request.method == 'POST':
        register_form = RegForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = register_form.cleaned_data.get('username','email')
            messages.success(request, 'Account with the username "' + user + '" was created successfully.')
            return redirect('login')
    else:
        register_form = RegForm()
        # messages.warning(request, 'Password does not match')
    return render(request, 'dashboard/signup.html', {'reg': register_form})
  
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Username Or password is incorrect')
    
    context = {}      
    return render(request, 'dashboard/signin.html', context)
@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html')

def UserDashboard(request):
    return render(request, 'User_Admin/index.html')

@login_required
def view_profile(request):
    template_name = 'dashboard/profile.html'
    profile = request.user
    return render(request, template_name, {'profile':profile})

class AddBlog(SuccessMessageMixin, CreateView):
    model = Blog
    form_class= BlogPost
    template_name = 'dashboard/addblog.html'
    success_url= reverse_lazy('addblog')
    success_message= 'Post added successfully'
    context_object_name= "addblog"

def viewBlog(request):
    # viewblogs= Blog.objects.all(request.user)
    return render(request, 'dashboard/view-blog.html')

class AddLike(LoginRequiredMixin, View):
    def blog(self, request, pk,*args, **kwargs):
        blog = Blog.objects.get(pk)

        is_dislike = False

        for dislike in blog.dislike.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            blog.dislikes.remove(request.user)
        
        is_like = False

        for like in blog.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            blog.likes.add(request.user)

        if not is_like:
            blog.likes.remove(request.user)
        
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def blog(self, request, pk, *args, **kwargs):
        blog = Blog.objects.get(pk)

        is_like = False

        for like in blog.dislike.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            blog.likes.remove(request.user)
        
        is_dislike = False

        for dislike in blog.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            blog.dislikes.add(request.user)
        if not is_dislike:
            blog.dislikes.remove(request.user)
        
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)




