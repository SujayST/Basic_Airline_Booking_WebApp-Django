from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from .forms import *
from django.utils import timezone
import datetime
# Create your views here.


def Home(request):

    all_books = airlines.objects.all()

    context = {
        'all_books': all_books
    }

    return render(request, 'home.html', context)


def bookticket1(request):

    if request.method == "POST":
        form = bookForm(request.POST)

        if form.is_valid():
            trn = bookticket()
            trn.transaction_id = form.cleaned_data["trn_id"]
            trn.User_id = form.cleaned_data["User_id"]
            trn.Airline_id = form.cleaned_data["Airline_id"]
            trn.issue_date = form.cleaned_data["issue_date"]
            trn.save()

    else:
        form = bookForm()

    allvideos = bookticket.objects.all()
    context = {
        'allvideos': allvideos,
    }

    return render(request, 'lendBook.html', locals())




def Aboutus(request):
    return render(request, 'contact.html')