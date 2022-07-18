# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    return render(request,"index.html")

def weather(request):
    return render(request,"weather.html")

def register(request):
    if request.method == 'POST':
        if request.POST['pw'] == request.POST['pw-confirm']:
            user = User (
                        user_id=request.POST['id'],
                        pwd=request.POST['pw'],
                        name=request.POST['name'],
                        gender=request.POST['gender'],
                        addr=request.POST['addr'],
                        birth=request.POST['birth'],
                        email=request.POST['email'],
                        )
            user.save()
            return redirect('/')
        return render(request, 'register.html')
    return render(request, 'register.html')

def login(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('user_id', None)
        login_password = request.POST.get('pwd', None)


        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            user = User.objects.get(user_id=login_username) 
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, user.pwd):
                request.session['user'] = user.id 
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('indexin.html')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'indexin.html',response_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def home(request):
    user_id = request.session.get('user')
    if user_id :
        user_info = User.objects.get(pk=user_id)
        return HttpResponse(user_info.user_id)
    
    return HttpResponse('로그인을 해주세요')

def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']

        board = Board(
            title=title,
            content=content,
            writer=writer,
        )
        board.save()
        return redirect('board')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm' : boardForm,
            'board': board,
        }

        return render(request, 'board.html', context)

def boardEdit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.writer = request.POST['writer']

        board.save()
        return redirect('board')

    else:
        boardForm = BoardForm
        return render(request, 'update.html',{'boardForm':boardForm})

def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')

def bd_edit(request):
    return render(request,'bd_edit.html')

def bd_list(request):
    return render(request,'bd_list.html')

def bd_view(request):
    return render(request,'bd_view.html')

def bd_write(request):
    return render(request,'bd_write.html')

def intro(request):
    return render(request,'intro.html')