from django.shortcuts import render
from .models import Company, EnergyConsumption
from .forms import EnergyConsumptionForm
from django.utils import timezone
# Create your views here.
def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        address = request.POST['address']
        phone_number = request.POST['phone_number']

        company = Company(name=name, email=email, website=website, address=address, phone_number=phone_number)
        company.save()


    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'index.html', context)

def energy(request):
   
    if request.method == 'POST':
        id = request.POST.get('company')
        company_id = int(id)
        company = Company.objects.get(id=company_id)
        amount = request.POST.get('amount')
        date_str = request.POST.get('date')

        date = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
        energy_consumption = EnergyConsumption(company=company,amount=amount,date=date)
        energy_consumption.save()

    context = {
        'energy_consumptions': EnergyConsumption.objects.all(),
        'companies': Company.objects.all(),
    }

    return render(request, 'energy.html', context)
