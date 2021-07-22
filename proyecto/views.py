from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import json
from django.http import JsonResponse
# Create your views here.
from .models import Movies

def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall()]
def add_condiciones(movie,fechai,fechaf,usuario):
    numf=0
    con=" and "
    c='"'
    select=""
    if movie or fechai or fechaf or usuario:
            select+=" where "
            if movie:
                filtro_movie= " movie="+c+movie+c
                select+=filtro_movie
                numf+=1
            if fechai and fechaf:
                filtro_fecha= " date BETWEEN " +c+fechai+c+ " and "+c+ fechaf +c
                if numf!=0: #agrege filtro movie
                    select+=con+filtro_fecha
                else: #no se envio filtro movie
                    select+=filtro_fecha
                    numf+=1
            if usuario:
                filtro_usuario=" user="+c+usuario +c
                if numf!=0: #  he enviado algun filtro anterior
                    select+=con+filtro_usuario
                else: #no he enviado ningun filtro anteriormente
                    select+=filtro_usuario
    return select
def index(request):
    print("REQUEST---------------",request.GET)
    movie=fechai=fechaf=usuario=""
    if request.method == 'GET': #esos if hay que quitar
        if('movie' in request.GET):
            movie= request.GET['movie']
            print("movieee...",str(movie))
        if('fechai' in request.GET):
            fechai=request.GET['fechai']
        if('fechaf' in request.GET):
            fechaf=request.GET['fechaf']
        if('user' in request.GET):
            usuario=request.GET['user']
        # numf=0
        # con=" and "
        # c='"' 
        cursor=connection.cursor()
        select= "select * from proyecto_movies  "
        select_filtro=add_condiciones(movie,fechai,fechaf,usuario)
        #agregando order by y limit 10
        select+=select_filtro+" order by score desc limit 10"
        print("SELECT TABLAA!!!! ",select)
        cursor.execute(select)
        print("????------- SELECT 1,---",select)
        results = dictfetchall(cursor)
        json_results = json.dumps(results,indent=4, default=str)
        
        #return myresult
        #people = Person.objects.raw('SELECT *, age(birth_date) AS age FROM myapp_person')
    # <view logic>
        #return JsonResponse(json_results,safe=False)
        return HttpResponse(json_results)
def top_menor_score(request):
    print("REQUEST---------------",request.GET)
    movie=fechai=fechaf=usuario=""
    if request.method == 'GET': #esos if hay que quitar
        if('movie' in request.GET):
            movie= request.GET['movie']
            print("movieee...",str(movie))
        if('fechai' in request.GET):
            fechai=request.GET['fechai']
        if('fechaf' in request.GET):
            fechaf=request.GET['fechaf']
        if('user' in request.GET):
            usuario=request.GET['user']
        # numf=0
        # con=" and "
        # c='"' 
        cursor=connection.cursor()
        select= "select * from proyecto_movies  "
        select_filtro=add_condiciones(movie,fechai,fechaf,usuario)
        #agregando order by y limit 10
        select+=select_filtro+" order by score asc limit 10"
        print("SELECT TABLAA!!!! ",select)
        cursor.execute(select)
        print("????------- SELECT 2,---",select)
        results = dictfetchall(cursor)
        json_results = json.dumps(results,indent=4, default=str)
        
        #return myresult
        #people = Person.objects.raw('SELECT *, age(birth_date) AS age FROM myapp_person')
    # <view logic>
        #return JsonResponse(json_results,safe=False)
        return HttpResponse(json_results)

def indicadores(request):
    print("REQUEST INDICADORES---------------",request.GET)
    # movie="", fechai="",fechaf="",usuario=""
    movie=fechai=fechaf=usuario=""
    if request.method == 'GET': #esos if hay que quitar
        if('movie' in request.GET):
            movie= request.GET['movie']
            print("movieee...",str(movie))
        if('fechai' in request.GET):
            fechai=request.GET['fechai']
        if('fechaf' in request.GET):
            fechaf=request.GET['fechaf']
        if('user' in request.GET):
            usuario=request.GET['user']
        # numf=0
        # con=" and "
        # c='"' 
        cursor=connection.cursor()
        select= "select  MIN(score) as min, MAX(score) as max , avg(score) as prom , count(distinct (user)) as users from proyecto_movies "
        select_filtro=add_condiciones(movie,fechai,fechaf,usuario)
        select+=select_filtro
        print("*******SELECT INDICADOR ---",select)  
        cursor.execute(select)
        #cursor.execute("select  MIN(score) as min, MAX(score) as max , avg(score) as prom , count(distinct (user)) as num from proyecto_movies")
        results = dictfetchall(cursor)
        json_results = json.dumps(results,indent=4, default=str)
        return HttpResponse(json_results)

def grafico(request):
    print("REQUEST GRAFICO---------------",request.GET)
    # movie="", fechai="",fechaf="",usuario=""
    movie=fechai=fechaf=usuario=""
    if request.method == 'GET': #esos if hay que quitar
        if('movie' in request.GET):
            movie= request.GET['movie']
            print("movieee...",str(movie))
        if('fechai' in request.GET):
            fechai=request.GET['fechai']
        if('fechaf' in request.GET):
            fechaf=request.GET['fechaf']
        if('user' in request.GET):
            usuario=request.GET['user']
        # numf=0
        # con=" and "
        # c='"' 
        cursor=connection.cursor()
        select= "select score, helpfulness, date from proyecto_movies "
        select_filtro=add_condiciones(movie,fechai,fechaf,usuario)
        select+=select_filtro+" order by date"
        print("*******SELECT GRAFICO ---",select)  
        cursor.execute(select)
        #cursor.execute("select  MIN(score) as min, MAX(score) as max , avg(score) as prom , count(distinct (user)) as num from proyecto_movies")
        results = dictfetchall(cursor)
        json_results = json.dumps(results,indent=4, default=str)
        return HttpResponse(json_results)