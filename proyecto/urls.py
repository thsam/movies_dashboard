from django.urls import path

from . import views
urlpatterns = [
    path("tab1", views.index, name="index"),
    path("pki",views.indicadores, name="indicadores"),
    path("tab2",views.top_menor_score, name="top_menor_score"),
    path("gra",views.grafico, name="grafico")

]