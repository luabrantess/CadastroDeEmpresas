from ctypes.wintypes import HENHMETAFILE
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Area, Cidade, Empresa, Produto, Telefone
from django.core import serializers
from django.http import JsonResponse

@csrf_exempt
def cidade(request):

    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
        data = Cidade(
            municipio=json_data.get("municipio", None),
            uf=json_data.get("uf", None)
        )
        data.save()
        return HttpResponse("201 - created", status=201)
    elif request.method == "GET":
        try:
            query = Cidade.objects.get(id=request.GET.get("id", None))
            return JsonResponse(json.loads(serializers.serialize('json', [query])), safe=False)
        except Cidade.DoesNotExist:
            return HttpResponse("404 - not found", status=404)
    else:
        return HttpResponse("405 - method not allowed", status=405)

def area(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
        data = Area(
            area = json_data.get("area", None)
        )
        data.save()
        return HttpResponse("201 - created", status=201)
    elif request.method == "GET":
        try:
            query = Area.objects.get(id=request.GET.get("id",None))
            return JsonResponse(json.loads(serializers.serialize('json',[query])), safe=False)
        except Area.DoesNotExist:
            return HttpResponse("404 - not found", status=404)
    else:
        return HttpResponse("405 - method not allowed", status=405)

def empresa(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
        data = Empresa(
            nome = json_data.get("nome", None),
            cidade = json_data.get("cidade", None),
            endereco = json_data.get("endereco", None),
            descricao = json_data.get("descricao", None),
            descricao_ingles = json_data.get("descricao_ingles", None),
            slogan = json_data.get("slogan", None),
            ponto_contato = json_data.get("ponto_contato", None),
            email = json_data.get("email", None),
            site = json_data.get("site", None),
        )
        data.save()
        return HttpResponse("201 - created", status= 201)
    elif request.method == "GET":
        try:
            query = Empresa.objects.get(id = request.GET.get("id", None))
            JsonResponse(json.loads(serializers.serialize('json', [query])), safe=False)
        except Empresa.DoesNotExist:
            return HttpResponse("404 - not found", status = 404)
    else:
        return HttpResponse("405 - method not allowed", status = 405)

def produto(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
        data = Produto(
            ident = json_data.get("ident", None),
            produto = json_data.get("produto", None)
        )
        data.save()
        return HttpResponse("201 - created", status = 201)
    elif request.method == "GET":
        try:
            query = Produto.objects.get(id = request.GET.get("id", None))
            JsonResponse(json.loads(serializers.serialize('json', [query])), safe=False)
        except Produto.DoesNotExist:
            return HttpResponse("404 - not found", status = 404)
        else:
            return HttpResponse("405 - method not allowed", status = 405)

def telefone(request):
    if request.method=="POST":
        json_data = json.loads(request.body)
        print(json_data)
        data = Telefone(
            ident = json_data.get("ident", None),
            telefone = json_data.get("telefone", None)
        )
        data.save()
        return HttpResponse("201 - created", status = 201)
    elif request.method == "GET":
        try:
            query = Telefone.objects.get(id = request.GET.get("id", None))
            JsonResponse(json.loads(serializers.serialize('json', [query])), safe=False)
        except Telefone.DoesNotExist:
            return HttpResponse("404 - not found", status = 404)
        else:
            return HttpResponse("405 - method not allowed", status = 405)


@csrf_exempt
def lista_cidade(request):
    if request.method == "GET":
        query = Cidade.objects.all()
        json_data = json.loads(serializers.serialize('json', query))
        response = []
        for i in json_data:
            response.append(i.get("fields", None))
        return JsonResponse(response, safe=False)
    else:
        return HttpResponse("405 - method not allowed", status=405)
