from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import View,TemplateView
from app.forms import *
#FBV for returning string as response

def fbv_string(request):
    return HttpResponse('This is FBv_string')

#CBV for returning string as response

class CbvString(View):
    def get(self,request):
        return HttpResponse('CBVstring')
    
#FBV to render html file and send context data   
def fbv_htmlpage(request):
    d={'name':'ASHU'}
    return render(request,'fbv_htmlpage.html',d)


#CBV to render html file and send context data
class CbvHtmlPage(View):
    def get(self,request):
        d={'name':'ASHU'}
        return render(request,'CbvHtmlPage.html',d)

#FBV to handle the djangoforms

def fbv_djnagoform(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))
    return render(request,'fbv_djnagoform.html',d)

#CBV to handle the djangoforms

class CbvDjangoForm(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'CbvDjangoForm.html',d)
    
    def post(self,request):
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))

    

















