from django.shortcuts import render


from django.views import generic


class Home (generic.TemplateView):
    template_name = 'bases/home.html'

class Shop(generic.TemplateView):
    
    template_name="bases/shop.html"

class Services(generic.TemplateView):
    
    template_name="bases/services.html"

class Contacts(generic.TemplateView):
    
    template_name="bases/contacts.html"