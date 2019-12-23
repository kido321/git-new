from django.shortcuts import render
from .models import Products,user
from .forms import Formmodel
from . import forms
def index (request):
   # product= Products.objects.all()
    return render(request ,'testt.html')#, {'product': product})

def resp (request):
    allProductss=Products.objects.all()
    mydic={'ppp':allProductss}
    #return HttpResponse({{love}},content=mydic)
    return render(request, 'index.html',context=mydic)

def userss(request):
    allusers=user.objects.all()
    userdic={'userkey':allusers}
    return render(request ,'userslist.html', context=userdic)



'''this is the forms views'''

def Fbview(request):
    formss= forms.FBformmodel()
    formsss = Formmodel()
    formdic={"fbkey":formsss}
    if request.method=='POST':
        formsss= forms.Formname(request.POST)
        if formsss.is_valid():
            formsss.save(commit=True)
    return render(request,'form2.html',{"formkey2":formsss})



def Formnameview2(request):
    formsss=Formmodel()
    if request.method=="POST":
        formsss=Formmodel(request.POST)
        if formsss.is_valid():
            formsss.save(commit=True)
            return userss(request)


    return render(request,'form.html',{"formkey2":formsss})

def facebook(request):
    return render(request,"form2.html")