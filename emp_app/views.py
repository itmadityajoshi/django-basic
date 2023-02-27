from django.shortcuts import render,HttpResponse
from .models import Employee, Roles, Department

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }

    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])

        new_user = Employee(first_name=first_name,
                            last_name=last_name,
                            dept_id=dept,
                            role_id=role,
                            salary=salary,
                            bonus=bonus,
                            phone=phone,)
        new_user.save()
        return HttpResponse('Employee Add successFully')
    

    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return render(request,"An Error Occured!")



def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successful")
        except:
            return HttpResponse("Please Enter A valid Employee ID")
    emps = Employee.objects.all()
    context = {
        "emps":emps
    }
    return render(request, 'remove_emp.html',context)


def search_emp(request):
    return render(request, 'search_emp.html')
