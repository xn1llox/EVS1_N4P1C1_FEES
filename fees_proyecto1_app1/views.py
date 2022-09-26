from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def noticia(request):
    return HttpResponse("<h3>Déficit habitacional afecta a 650 mil familias:</h3> <br>2 millones de personas,</br> <mark>sin vivienda propia</mark> Una cruda realidad sobre la <cite>crisis habitacional</cite> conocimos anoche en el tercer capítulo de <mark>Informe Especial.</mark> Y este jueves la fundación Déficit Cero expuso una cifra alarmante: más de 400 mil personas están en peligro de quedarse sin un hogar.</h3>")

def juegos(request):
    return HttpResponse("<h3>Filtración GTA 6: Nueva información sobre el supuesto autor del hackeo:</h3> <br>La policía de Londres</br> afirma que el joven hacker, quien <mark>pertenecería a un grupo conocido como Lapsus$</mark>, compareció ante el Tribunal de <cite>Menores de Highbury Corner<cite> el pasado sábado 24 de septiembre.")