from django.urls import path, re_path
from .views import lista_cidade, cidade

urlpatterns = [
    path('api/cidade', cidade, name='cidade'),  # GET / POST API
    path('api/cidades', lista_cidade, name='lista_cidades')  # LIST (GET) API
]
