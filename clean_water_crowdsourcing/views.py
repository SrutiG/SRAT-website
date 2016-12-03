from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from clean_water_crowdsourcing.models import Account
from clean_water_crowdsourcing.models import WaterPurityReport
from clean_water_crowdsourcing.models import WaterSourceReport
from django.core.exceptions import ObjectDoesNotExist
from django.template.defaulttags import csrf_token




def index(request):
    if not request.session.get('login'):
        return redirect('login')
    else:
        return redirect('main')

def login(request):
    request.session['login'] = False
    request.session['username'] = None
    request.session['user'] = False
    request.session['worker'] = False
    request.session['manager'] = False
    request.session['admin'] = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            account = Account.objects.get(username = username, password = password)
            request.session['login'] = True
            request.session['username'] = account.username
            if account.account_type == 'User':
                request.session['user'] = True
            elif account.account_type == 'Worker':
                request.session['user'] = True
                request.session['worker'] = True
            elif account.account_type == 'Manager':
                request.session['user'] = True
                request.session['worker'] = True
                request.session['manager'] = True
            elif account.account_type == 'Administrator':
                request.session['admin'] = True
            return redirect('main')
        except ObjectDoesNotExist:
            return redirect('login')
    return render(request, 'clean_water_crowdsourcing/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        streetName = request.POST.get('streetName')
        cityName = request.POST.get('cityName')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        phone = request.POST.get('phone')
        accountType = request.POST.get('type')

        Account.objects.create(first_name = firstname, last_name = lastname, username = username,
                               password = password, address_street = streetName, address_city = cityName,
                               address_zip = zip, address_state = state, phone = phone, account_type = accountType)
        return redirect('login')
    return render(request, 'clean_water_crowdsourcing/register.html')


def main(request):
    username = request.session.get('username')
    user = request.session.get('user')
    worker = request.session.get('worker')
    manager = request.session.get('manager')
    admin = request.session.get('admin')
    account = Account.objects.get(username=username)
    sourceReports = WaterSourceReport.objects.all()
    return render(request, 'clean_water_crowdsourcing/main.html', {'username': username, 'user': user, 'worker': worker,
                                                                   'manager': manager, 'admin': admin, 'sourceReports': sourceReports})