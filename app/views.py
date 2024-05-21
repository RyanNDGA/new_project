from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.template import loader

from .models import student
from django.http import HttpResponse


def addstudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        storename = request.POST.get('storename')
        contactnumber = request.POST.get('contactnumber')
        storeaddress = request.POST.get('storeaddress')

        obj1 = student(Name=name, Email=email, Store_name=storename, contact_number=contactnumber,
                       store_address=storeaddress)
        obj1.save()

        mydata = student.objects.all()
        context = {'stores': mydata}
        return render(request, 'add_students.html', context)
    else:
        return render(request, 'add_students.html')


def updatestudent(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        storename = request.POST.get('storename')
        contactnumber = request.POST.get('contactnumber')
        storeaddress = request.POST.get('storeaddress')

        editestore = student.objects.get(id=id)
        editestore.Name = name
        editestore.Email = email
        editestore.Store_name = storename
        editestore.contact_number = contactnumber
        editestore.store_address = storeaddress
        editestore.save()

    return redirect('/stores')


def edit_student(request, id):
    data = student.objects.get(id=id)
    context = {'data': data}
    return render(request, 'student_dashboard.html', context)


# Create your views here.
def students(request):
    mydata = student.objects.all()
    context = {'stores': mydata}
    return render(request, 'add_students.html', context)


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        storename = request.POST.get('storename')
        contactnumber = request.POST.get('contactnumber')
        storeaddress = request.POST.get('storeaddress')

        obj1 = student(Name=name, Email=email, Store_name=storename, contact_number=contactnumber,
                       store_address=storeaddress)
        obj1.save()

        mydata = student.objects.all()
        context = {'stores': mydata}
        return render(request, 'add_students.html', context)
    else:
        return render(request, 'add_students.html')


def delete_store(request, id):
    deletestore = student.objects.get(id=id)
    deletestore.delete()
    return redirect('/stores')

def stores(request):
    mydata = student.objects.all()
    context = {'stores': mydata}
    return render(request, 'add_students.html', context)
