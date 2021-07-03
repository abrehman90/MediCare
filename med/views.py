from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')


@login_required()
def ngo(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        ngoname = request.POST['ngoname']
        ngonumber = request.POST['ngonumber']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        medicine = request.POST['medicine']
        medicinedate = request.POST['medicinedate']
        medicineqty = request.POST['medicineqty']
        medicinetype = request.POST['medicinetype']
        phone = request.POST['phone']
        zipcode = request.POST['zipcode']
        cardname = request.POST['cardname']
        cardnumber = request.POST['cardnumber']
        month = request.POST['month']
        year = request.POST['year']
        civ = request.POST['civ']
        print(city,civ,medicinetype)
        con = NGO(name=name,email=email,ngoname=ngoname,ngonumber=ngonumber,address=address,country=country,city=city,medicine=medicine,medicinedate=medicinedate,medicineqty=medicineqty,medicinetype=medicinetype,phone=phone,zipcode=zipcode,cardname=cardname,cardnumber=cardnumber,month=month,year=year,civ=civ)
        con.save()
        return render(request,'index.html')
    return render(request,'ngo.html')


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        medicine = request.POST['medicine']
        medicinedate = request.POST['medicinedate']
        medicineqty = request.POST['medicineqty']
        medicinetype = request.POST['medicinetype']
        phone = request.POST['phone']
        zipcode = request.POST['zipcode']
        cardname = request.POST['cardname']
        cardnumber = request.POST['cardnumber']
        month = request.POST['month']
        year = request.POST['year']
        civ = request.POST['civ']
        print(city,civ,medicinetype)
        con = Buy(name=name,email=email,address=address,country=country,city=city,medicine=medicine,medicinedate=medicinedate,medicineqty=medicineqty,medicinetype=medicinetype,phone=phone,zipcode=zipcode,cardname=cardname,cardnumber=cardnumber,month=month,year=year,civ=civ)
        con.save()
        return render(request,'index.html')
    return render(request,'form.html')


def card(request):
    if request.method == 'POST':
        cardname = request.POST['cardname']
        cardnumber = request.POST['cardnumber']
        month = request.POST['month']
        year = request.POST['year']
        civ = request.POST['civ']
        con = CardDetail(cardname=cardname,cardnumber=cardnumber,month=month,year=year,civ=civ)
        con.save()
        return render(request,'index.html')
    return render(request,'donation.html')


def blog(request):
    return render(request,'blog.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        con = Contact(name=name,email=email,message=message)
        con.save()
        return render(request,'contact.html')
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')
