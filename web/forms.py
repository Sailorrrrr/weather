from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *



class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title','content','writer']
