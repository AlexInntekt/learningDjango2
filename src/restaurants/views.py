from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

#for fetching saved data:
from .models import RestaurantsLocation

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

def restaurants_listview(request):
      template_name = 'restaurants/restaurants_list.html'
      queryset = RestaurantsLocation.objects.all()
      context = { "objects_list": queryset }
      return render(request, template_name, context)
   
      
   
   
'''
class ContactView(View):
 def get(self, request, *args, **kwargs):
   context = {}
   print(kwargs)
   return render(request, "home3.html", context)
'''

class ContactView(TemplateView):
  template_name = 'home3.html'

class ContactTemplateView(TemplateView):
  template_name = 'home3.html'
  
  def get_context_data(self, *args, **kwargs):
      context = super(TemplateView, self).get_context_data(*args, **kwargs)
      print("▲ Context: ▲ ",context)
      return context
   
class RestaurantsListView(ListView):
      queryset = RestaurantsLocation.objects.all()
      template_name = 'restaurants/restaurants_list.html'
      context = {
                   "object_list" : queryset
      }
	  
class MexicanRestaurantsListView(ListView):
      queryset = RestaurantsLocation.objects.filter(category__iexact='mexican')
      template_name = 'restaurants/restaurants_list.html'
      context = {
                   "object_list" : queryset
      }
	  
class ItalianRestaurantsListView(ListView):
      queryset = RestaurantsLocation.objects.filter(category__iexact='italian')
      template_name = 'restaurants/restaurants_list.html'
      context = {
                   "object_list" : queryset
      }	  
	  

	  
	  
   
      
   
   
   
   
   
   