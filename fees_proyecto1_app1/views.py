from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def noticia(request):
    return HttpResponse("<h3>Déficit habitacional afecta a 650 mil familias:</h3> <br>2 millones de personas,</br> <mark>sin vivienda propia</mark> Una cruda realidad sobre la <cite>crisis habitacional</cite> conocimos anoche en el tercer capítulo de <mark>Informe Especial.</mark> Y este jueves la fundación Déficit Cero expuso una cifra alarmante: más de 400 mil personas están en peligro de quedarse sin un hogar.</h3>")

def deporte(request):
    return HttpResponse("<h3>Candidato a presidencia de Emelec:</h3> Para Quinteros la prioridad es <cite>Colo Colo Carlos Torres<cite> explicó que el <mark>DT albo es una de las opciones</mark> que manejan.")