from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def informe(request):
    return HttpResponse("<h2>Renunció el tercer hombre del Ejército por filtración de correos de las FF.AA.,</h2> <br>El general Guillermo Paiva presentó su renuncia esta tarde como jefe del Estado Mayor Conjunto, luego de la filtración de más de <div>400 mil correos electrónicos<div> enviados por <cite>funcionarios</cite> de las <mark>Fuerzas Armadas, policías y Gobierno.</mark> Documentos reservados de la inteligencia militar, personales e incluso antecedentes diplomáticos salieron a la luz pública.</br>")

def juegos(request):
    return HttpResponse("<h2>Filtración GTA 6:</h2> <br>Nueva información sobre el supuesto autor del hackeo.<br> <mark>La policía de Londres afirma que el joven hacker</mark> quien pertenecería a un grupo conocido como <div>Lapsus$<div>, compareció ante el <cite>Tribunal de Menores de Highbury Corner</cite> el pasado sábado 24 de septiembre.")
