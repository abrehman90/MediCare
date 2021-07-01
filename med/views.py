from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request,'ngo.html')


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        country = request.POST['country']
        medicine = request.POST['medicine']
        phone = request.POST['phone']
        zipcode = request.POST['zipcode']
        con = Addres(name=name,email=email,address=address,country=country,medicine=medicine,phone=phone,zipcode=zipcode)
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
        print(cardnumber,civ)
        con = CardDetail(cardname=cardname,cardnumber=cardnumber,month=month,year=year,civ=civ)
        print(con)
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
