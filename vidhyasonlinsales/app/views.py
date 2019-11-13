from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Admin,Merchant,Product
import random,json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View

# Create your views here.
def adminlogin(request):
    return render(request,"adminlogin.html")


def Validate(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    up = Admin.objects.filter(username=username,password=password)

    if up:
         return render(request,"adminwelcome.html",{"msg":" Welcome Admin"})


def addmerchant(request):
    return render(request,"addmerchant.html")


def viewmerchant(request):
    m = Merchant.objects.all()
    return render(request,"viewmerchant.html",{"data":m})


def deletemerchant(request):
    Merchant.objects.filter().delete()
    return render(request,"deletemarchant.html",{"msg":"Merchant was deleted"})


def addmrc(request):
    idno = random.randint(1000, 9999)
    name = request.POST.get("name")
    cno = request.POST.get("contantno")
    email_id = request.POST.get("email_id")
    password = random.randint(10000, 99999)
    Merchant(idno=idno, name=name, contantno=cno, email_id=email_id, password=password).save()
    return render(request, "adminwelcome.html", {"msg": "Merchant Was added"})


@method_decorator(csrf_exempt,name='dispatch')
class Writeone(View):
    def post(self,request):
        data = request.body
        print(data)

        jd = json.loads(data)

        print(jd)
        email=''
        password=''
        for x in jd:
         # print(x,jd[x])
            if x=='emailid':
                email=jd[x]

            else:
                password=jd[x]
        d=Merchant.objects.filter(emailid=email, password=password)
        if d:
            js = json.dumps({"msg": "valid Details"})
            return HttpResponse(js, content_type="application/json")
        else:
            js = json.dumps({"msg": "Invalid Details"})
            return HttpResponse(js, content_type="application/json")

from django.core.serializers import serialize
class Readone(View):
    def get(self,request):
        qs=Merchant.objects.all()
        json_data=serialize("json",qs,fields=('emailid','password'))
        return HttpResponse(json_data,content_type="application/json")

@method_decorator(csrf_exempt,name='dispatch')
class Addproduct(View):
    def post(self,request):
        data = request.body
        print(data)
        jd = json.loads(data)
        print(jd)
        no=jd["no"]
        name=jd["name"]
        price=jd["price"]
        quantity=jd["quantity"]


        print(jd["no"])
        ef=Product(no=no,name=name,price=price,quantity=quantity).save()

        js = json.dumps({"msg": "product is saved"})
        return HttpResponse(js, content_type="application/json")

@method_decorator(csrf_exempt,name='dispatch')
class Changepwd(View):
    def post(self,request):
        data = request.body
        print(data)
        jd = json.loads(data)
        print(jd)
        email=jd['email']
        old=jd['old']
        new=jd['new']
        confirm=jd['confirm']
        if new==confirm:
            p=Merchant.objects.filter(emailid=email,password=old).update(password=confirm)
            print(p)
        else:
            js = json.dumps({"msg": "False"})
            return HttpResponse(js, content_type="application/json")
        if p:
            js = json.dumps({"msg": "password changed"})
            return HttpResponse(js, content_type="application/json")
        else:
            js = json.dumps({"msg": "0"})
            return HttpResponse(js,content_type="application/json")

