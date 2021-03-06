from django.shortcuts import render
from django.shortcuts import redirect
from clean_water_crowdsourcing.models import Account
from clean_water_crowdsourcing.models import WaterPurityReport
from clean_water_crowdsourcing.models import WaterSourceReport
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse




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
        email = request.POST.get('email')
        password = request.POST.get('password')
        streetName = request.POST.get('streetName')
        cityName = request.POST.get('cityName')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        phone = request.POST.get('phone')
        accountType = request.POST.get('type')

        Account.objects.create(first_name = firstname, last_name = lastname, email=email, username = username,
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
    purityReports = WaterPurityReport.objects.all()
    return render(request, 'clean_water_crowdsourcing/main.html', {'username': username, 'user': user, 'worker': worker,
                                                                   'manager': manager, 'admin': admin, 'account': account,
                                                                   'sourceReports': sourceReports, 'purityReports': purityReports})
@csrf_exempt
def addReport(request):
    username = request.session.get('username')
    account = Account.objects.get(username=username)
    water_source_location = request.POST.get('water-source-address')
    water_source_type = request.POST.get('water-source-type')
    water_source_condition = request.POST.get('water-source-condition')
    WaterSourceReport.objects.create(reporter_name=account, water_type=water_source_type, water_location = water_source_location
                                     , water_condition = water_source_condition)
    return redirect('main')

@csrf_exempt
def addPurityReport(request):
    username = request.session.get('username')
    account=Account.objects.get(username=username)
    water_location = request.POST.get('water-purity-address')
    water_purity_condition = request.POST.get('water-purity-condition')
    virus_PPM = request.POST.get('virus-ppm')
    contaminant_PPM = request.POST.get('contaminant-ppm')
    wsr = WaterSourceReport.objects.get(water_location = water_location)
    WaterPurityReport.objects.create(reporter_name = account, water_location = wsr, water_condition = water_purity_condition,
                                     virus_ppm = virus_PPM, contaminant_ppm = contaminant_PPM)
    return redirect('main')

@csrf_exempt
def editProfile(request):
    username = request.session.get('username')
    account = Account.objects.get(username=username)
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    address_street = request.POST.get('address_street')
    address_city = request.POST.get('address_city')
    address_zip = request.POST.get('address_zip')
    address_state = request.POST.get('address_state')
    phone = request.POST.get('phone')
    account.first_name = first_name
    account.last_name = last_name
    account.email = email
    account.address_city = address_city
    account.address_state = address_state
    account.address_zip = address_zip
    account.address_street = address_street
    account.phone = phone
    account.save()
    return redirect('main')


def deleteReport(request, reportNum):
    instance = WaterSourceReport.objects.get(report_number = reportNum)
    instance.delete()
    return redirect('main')

def getPurityReports(request, location):
    response_data = {}
    reports = []
    address = request.GET.get('location')
    purityLocations = WaterPurityReport.objects.filter(water_location = address)
    for item in purityLocations:
        reports.append({"date": str(item.report_date), "virus_ppm":item.virus_ppm,
                        "contaminant_ppm":item.contaminant_ppm, "max" : max(item.virus_ppm, item.contaminant_ppm)})
    response_data["reports"] = reports
    response = JsonResponse(response_data)
    return response
