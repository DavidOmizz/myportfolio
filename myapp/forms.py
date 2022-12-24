
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, label = 'Name', widget= forms.TextInput(attrs={'placeholder':'Enter full name', 'class': 'form-control'}))
    email = forms.EmailField(required=True,label = 'email', widget= forms.TextInput(attrs={'placeholder':'Enter your mail', 'class': 'form-control'}))
    subject = forms.CharField(required=True,label = 'subject', widget= forms.TextInput(attrs={'placeholder':'Subject', 'class': 'form-control'}))
    message = forms.CharField(required=True,label = 'message', widget= forms.Textarea(attrs={'placeholder':'Message', 'class': 'form-control'}))
    class Meta:
        model =Contact
        fields = ('name', 'email', 'subject', 'message')


class CommentForm(forms.ModelForm):
    name = forms.CharField(label = 'name', widget= forms.TextInput(attrs={'placeholder':'Enter full name', 'class': 'form-control'}))
    email = forms.EmailField(label = 'email', widget= forms.TextInput(attrs={'placeholder':'Enter your mail', 'class': 'form-control'}))
    content = forms.CharField(label = 'content', widget= forms.Textarea(attrs={'placeholder':'Message', 'class': 'form-control'}))
    class Meta:
        model =Comment
        fields = ('name', 'email', 'content')

class RegForm(UserCreationForm):
    username = forms.CharField(label = 'username', widget= forms.TextInput(attrs={'placeholder':'Enter username', 'class': 'form-control'}))
    first_name = forms.CharField(label = 'first_name', widget= forms.TextInput(attrs={'placeholder':'Enter full name', 'class': 'form-control'}))
    last_name = forms.CharField(label = 'last_name', widget= forms.TextInput(attrs={'placeholder':'Enter last name', 'class': 'form-control'}))
    email = forms.EmailField(label = 'email', widget= forms.TextInput(attrs={'placeholder':'Enter full name', 'class': 'form-control'}))
    password1 = forms.CharField(label = 'password1', widget= forms.TextInput(attrs={'placeholder':'Password', 'class': 'form-control'}))
    password2 = forms.CharField(label = 'password2', widget= forms.TextInput(attrs={'placeholder':'Re-enter password', 'class': 'form-control'}))
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('image', 'category', 'title', 'body', 'duration', 'status')