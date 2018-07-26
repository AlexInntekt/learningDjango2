"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from restaurants.views import home, home2, home3, ContactTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
	path('home',home, name='home'),
	path('home2',home2, name='home2'),
	path('home3',home3, name='home3'),
	path('ContactTemplateView/',ContactTemplateView.as_view(), name='ContactTemplateView'),
]


#/<int:id>















