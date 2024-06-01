from django.shortcuts import render, redirect
from .models import StudentDB
from django.contrib import messages


# Create your views here.
def index(request):
    data=StudentDB.objects.all()
    context={"data":data}
    return render(request,"index.html", context)

def about(request):
    return render(request,"about.html")


# Insert Operation
def insertData(request):
        if request.method == "POST":
            name=request.POST.get('completename')
            email=request.POST.get('completeemail')
            gender=request.POST.get('gender')
            phone=request.POST.get('completephone')
            address=request.POST.get('completeaddress')

            print(name, email,gender, phone, address)

            query =StudentDB(name=name, email=email, gender=gender, phone=phone, address=address)
            query.save()
            messages.info(request, "Data Inserted Successfully")
            return redirect("/")
        return render(request,"index.html")


# Updation of Data
def updateData(request, id):
        
        if request.method == "POST":
            name=request.POST['completename']
            email=request.POST['completeemail']
            gender=request.POST['gender']
            phone=request.POST['completephone']
            address=request.POST['completeaddress']
            edit= StudentDB.objects.get(id=id)
            edit.name=name
            edit.email=email
            edit.gender=gender
            edit.phone=phone
            edit.address=address
            edit.save()
            messages.warning(request, "Data Updated Successfully")
            return redirect("/")

        d= StudentDB.objects.get(id=id)
        context={"d" : d}
        return render(request,"update.html",context)


# Delete Operation
def deleteData(request, id):
    d=StudentDB.objects.get(id=id)
    d.delete()
    messages.error(request, "Data Deleted Successfully")
    return redirect("/")
