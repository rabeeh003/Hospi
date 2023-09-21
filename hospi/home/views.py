from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Doctors
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request,"home.html")
def department(request):
    dic_dipart = {
        "dept":Department.objects.all()
    }
    return render(request,"department.html",dic_dipart)
def contact(request):
    return render(request,"contact.html")
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conform.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request,"booking.html",dict_form)
def doctor(request):
    dic_doct = {
        "doct":Doctors.objects.all()
    }
    return render(request,"doctors.html",dic_doct)
def about(request):
    return render(request,"about.html")