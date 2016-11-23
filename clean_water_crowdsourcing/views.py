from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect



def index(request):
    if not request.session.get('login'):
        return redirect('login')
    else:
        return redirect('main')

def login(request):
    request.session['login'] = False
    request.session['username'] = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "user" and password == "pass":
            request.session['login'] = True
            request.session['username'] = username
            return redirect('main')
        else:
            return redirect('login')
    return render(request, 'clean_water_crowdsourcing/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        return redirect('login')
    return render(request, 'clean_water_crowdsourcing/register.html')


def main(request):
    user = request.session.get('username')
    return render(request, 'clean_water_crowdsourcing/main.html')