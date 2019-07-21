# restaurantes/views.py

from django.shortcuts import render, HttpResponse
from .models import restaurantes
from .forms import RestauranteForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
# Create your views here.

def index(request):
    context = {}   
    return render(request,'index_no_login.html', context)


@login_required
def restaurante(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'index_login.html', context)

def nuevo_restaurante(request):

   form = RestauranteForm()

   print ('hola')
   if request.method == 'POST':
      form = RestauranteForm(request.POST)
      if form.is_valid():                   # se pasan los validadores
         datos = form.cleaned_data

         client = MongoClient()

         db = client.test
#Bakery
# AIzaSyBmHo8iHNZo6s7022aiZbmxFlhrW6-D7v4 
         db.restaurantes.insert({
          'name': datos['name'],
          'cuisine': datos['cuisine'],
          'addres': {'zipcode': datos['zipcode']}
          })


         '''cursor = db.restaurantes.find({'cuisine':datos['cuisine']})

         for c in cursor:
          print(c)
         print(datos)'''
         
         return redirect('/restaurantes/restaurante')

   # GET o error de validación
   context = {
      'form': form,              # en blanco o rellena con errores
   }
   return render(request, 'nuevo_restaurante_form.html', context)

def map_restaurante(request):

   form = RestauranteForm()

   print ('hola map')
   if request.method == 'POST':
      form = RestauranteForm(request.POST)
      if form.is_valid():                   # se pasan los validadores
         datos = form.cleaned_data

         client = MongoClient()

         db = client.test

#Bakery
# AIzaSyBmHo8iHNZo6s7022aiZbmxFlhrW6-D7v4 

#Accra Restaurant             African         10453

         cursor = db.restaurantes.find({'name':datos['name'],'cuisine':datos['cuisine']})

         busqueda = [ i for i in cursor]
         zipcodes = [ int(i['address']['zipcode']) for i in busqueda]

         lat, lon = None, None
         for i in range(len(zipcodes)):
          if int(datos['zipcode']) == int(zipcodes[i]):
            lat = busqueda[i]['address']['coord'][1]
            lon = busqueda[i]['address']['coord'][0]
         
         context = { 'titulo': datos['name']+','+str(datos['zipcode']),'lat': lat, 'lon': lon }

         if lat == None:
          context = {'titulo': 'No se encuentra el restaurante '+datos['name']+','+str(datos['zipcode'])}
         return render(request, 'map_restaurante.html', context)

   # GET o error de validación
   context = {
      'form': form,              # en blanco o rellena con errores
   }
   return render(request, 'map_restaurante_form.html', context)



def grafica_restaurante(request):


         client = MongoClient()

         db = client.test

#Bakery
# AIzaSyBmHo8iHNZo6s7022aiZbmxFlhrW6-D7v4 

#Accra Restaurant             African         10453
  
         t_cocina = db.restaurantes.distinct('cuisine')
         t_cocina.sort()
         print('b1')

         grafica = []
         for tc in t_cocina:
          cursor_tc = db.restaurantes.find({'cuisine':tc})
          grafica.append({'tc':tc, 'ntc':cursor_tc.count()})
          print(tc,cursor_tc.count())

         print('b2',len(grafica))
         
         context = {'grafica':grafica }

        
         return render(request, 'grafica_restaurante.html', context)
