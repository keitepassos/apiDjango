from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('estado', EstadoListView.as_view()),  
    path('estado/<int:id>', EstadoDetailView.as_view()),
    path('municipio', MunicipioListView.as_view()),
    path('municipio/<int:id>', MunicipioDetailView.as_view()),   
    path('testeQuery', TesteViewQuery.as_view())  
]