from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

def sign_up_by_django(request):
    users = ['Ivan', 'Egor', 'Marina']
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            for user in users:
                if user == username:
                    info['Error']='Пользователь уже существует'
                    return render(request, 'registration_page.html', info)
                else:
                    continue
            if password == repeat_password and age >= 18:
                users.append(username)
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['Error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', info)
            elif age < 18:
                info['Error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {form: 'form'})

def sign_up_by_html(request):
    users = ['Ivan', 'Egor', 'Marina']
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            for user in users:
                if user == username:
                    info['Error'] = 'Пользователь уже существует'
                    return render(request, 'registration_page.html', info)
                else:
                    continue
            if password == repeat_password and age >= 18:
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['Error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', info)
            elif age < 18:
                info['Error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {form: 'form'})