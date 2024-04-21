from django.http import HttpResponse
import datetime
from django.shortcuts import render
def home(request):
    isActive=True
    if request.method=='POST':
        check=request.POST.get("check")
        print(check)
        if check is not None: 
            isActive=True
        else: isActive=False

    date= datetime.datetime.now()
    name="LearnCodeWithDurgesh"
    list_of_programs=[
        'Wap to check even or odd',
        'Wap to check prime numbers',
        'Wap to print all prime numbers from 1 to 100',
        'Wap to print pascals triangle'
    ]
    student={
        'student_name':"Rahul",
        'student_college':"ZYZ",
        'student_city':'DELHI'
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    # print("this function is called from view index")
    # # return HttpResponse("<h1> Hello this is index page </h1>"+str(date))
    return render(request,"home.html",data)

def about(request):

    print("test function is called from view")
    # return HttpResponse("<h1> Hello this is test page </h1>")
    return render(request,"home.html",{})


def services(request):
    # return HttpResponse("<h1>this is services page</h1>")
    return render(request,"services.html",{})
