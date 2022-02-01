"""
Definition of views.
"""

from datetime import datetime
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from app.models import Departments, Designations, Employees

def home(request):
    """Renders the home page."""
    department=Departments.objects.all()
    designation=Designations.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request,'app/index.html',{
                                            'title':'Home Page',
                                            'department':department,
                                            'designation':designation,
                                            'year':datetime.now().year,
                                            
                                           })
def registrationsave(request):
    if request.method !="POST":
        return HttpResponse('Method Not allowed')
    else:
        name=request.POST.get("name")
        age=request.POST.get("age")
        department_id=request.POST.get("department")
        department=Departments.objects.get(id=department_id)
        designation_id=request.POST.get("designation")
        designation=Designations.objects.get(id=designation_id)
        salary=request.POST.get("salary")
        try:
            emp=Employees(name=name,age=age,department=department,designation=designation,salary=salary)
            emp.save()
            messages.success(request,"Successfully Added Employee")
            return HttpResponseRedirect(reverse("home"))
        except Exception as e:
            print(e)
            messages.error(request,"Failed To Add employee")
            return HttpResponseRedirect(reverse("home"))


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
    

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
