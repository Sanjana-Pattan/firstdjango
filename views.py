from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Sanjana, Sanjana1



# Create your views here.
def San(request):
   if request.method == 'POST':
        a= request.POST.get("name")
        b = request.POST.get("address")
        c= request.POST.get("empID")
        e = Sanjana(name=a,address=b,empID=c)
        e.save()
        print(a)
   else:

         return render(request,"page1.html",context={})
   return HttpResponse("printed on Console, please Check!!")



# def func(request):
#    if request.method == 'POST':
#         Name= request.POST.get("nm")
#         Address= request.POST.get("add")
#         City= request.POST.get("city")
#         PINCODE= request.POST.get("pin")
#         print(Name,Address,City,PINCODE)
#    return HttpResponse("Check Console")





# def func2(request):
#    a = Sanjana()
#    a=Sanjana.objects.get(empID=111)
#    print(a)
#    return render(request,"page1.html",context={"name":"Sanj"})
    
  