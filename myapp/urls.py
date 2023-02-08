from . import views
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user-dashboard/', views.UserDashboard, name = 'user-dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('addblog/', views.AddBlog.as_view(), name= 'addblog'),
    path('viewBlog/', views.viewBlog, name="viewBlog"),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('bloglist/', views.blog_list, name='bloglist'),
    path('<slug:slug>/', views.blog_single, name='blog-single'),
    path('portfolio/<slug:slug>', views.portfolio_single, name='port'),
    path('blog/<int:pk>/like', AddLike.as_view(), name='like'),
    path('blog/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('profile', views.view_profile, name = 'profile'),
    # path('search-blogs', views.BlogSearchView.as_view(), name = 'search_blogs'),

]