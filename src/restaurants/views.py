from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def homeOnTheSpot(request):
 html_var = '398'
 html_ = f"""<!DOCTYPE html>
 <html lang=en>

 <head>
 </head>
 <body>
 <h1>Hello from django! {html_var}</h1>
 </body>
 </html>
 """
 return HttpResponse(html_)
 
 
contextOne = {"svar2": True , "index":1}
contextTwo = {"svar2": True , "index":2}
contextThree = {"svar2": True , "index":3}
 
def home(request):
   return render(request, "base.html",contextOne)
   
def home2(request):
   return render(request, "home2.html", contextTwo)
   
def home3(request):
   return render(request, "home3.html", contextThree)

 
class ContactView(View):
 def get(self, request, *args, **kwargs):
   context = {}
   print kwargs
   return render(request, "home3.html", context)

   
   

   
   
   
   
   
   
   
   
   
   
   
   
   