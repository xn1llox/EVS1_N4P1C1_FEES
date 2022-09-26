from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def informe(request):
    return HttpResponse("<h2>Renunció el tercer hombre del Ejército por filtración de correos de las FF.AA.,</h2> <br>El general Guillermo Paiva presentó su renuncia esta tarde como jefe del Estado Mayor Conjunto, luego de la filtración de más de <div>400 mil correos electrónicos<div> enviados por <cite>funcionarios</cite> de las <mark>Fuerzas Armadas, policías y Gobierno.</mark> Documentos reservados de la inteligencia militar, personales e incluso antecedentes diplomáticos salieron a la luz pública.</br>")

def deporte(request):
    return HttpResponse("<h2>Colo Colo puede gritar campeón ante la UC: la programación de la fecha 26 del Campeonato Nacional:</h2>  <cite>Esta es la programación de la 26ª fecha</cite> del <mark>Campeonato Nacional.</mark> Una jornada donde Colo Colo <div>podría bajar la estrella 33</div> en el fútbol chileno")

