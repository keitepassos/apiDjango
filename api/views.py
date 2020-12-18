from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .serializers import *
from AppTeste.models import *

class EstadoListView(APIView):
    def get(self, request):
        try:
            listaCaracteres = Estado.objects.all()
            serial = EstadoSerializer(listaCaracteres, many=True)
            return Response(serial.data)
        except Exception:
            return JsonResponse({'mensagem': 'Falha ao listar Estado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        serial = EstadoSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)

class EstadoDetailView(APIView):
    def get(self, request, id):
        try:
            if id=="0":
                return JsonResponse({"mensagem":"o id precisa ser maior que 0"}, status=status.HTTP_400_BAD_REQUEST) 
            estado = Estado.objects.get(id=id)
            serializer = EstadoSerializer(estado)
            return Response(serializer.data)
        except Estado.DoesNotExist:
            return JsonResponse({"mensagem":"Estado existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem":f"erro interno servidor com id {id}"+str(Exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            estado = Estado.objects.get(id=id)
            estado.descricao = request.data["descricao"]
            estado.uf = request.data["uf"]
            
            estado.save()

            serial = EstadoSerializer(data=model_to_dict(estado))
            serial.is_valid()
            return Response(serial.data, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'mensagem': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class MunicipioListView(APIView):
    def get(self, request):
        try:
            listaCaracteres = Municipio.objects.all()
            serial = MunicipioSerializer(listaCaracteres, many=True)
            return Response(serial.data)
        except Exception:
            return JsonResponse({'mensagem': 'Falha ao listar Municipio'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        serial = MunicipioSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)

class MunicipioDetailView(APIView):
    def get(self, request, id):
        try:
            if id=="0":
                return JsonResponse({"mensagem":"o id precisa ser maior que 0"}, status=status.HTTP_400_BAD_REQUEST) 
            municipio = Municipio.objects.get(id=id)
            serializer = MunicipioSerializer(municipio)
            return Response(serializer.data)
        except Municipio.DoesNotExist:
            return JsonResponse({"mensagem":"Municipio existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem":f"erro interno servidor com id {id}"+str(Exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            municipio = Municipio.objects.get(id=id)
            municipio.descricao = request.data["descricao"]
            municipio.area = request.data["area"]
            municipio.populacao = request.data["populacao"]
            
            municipio.save()

            serial = MunicipioSerializer(data=model_to_dict(municipio))
            serial.is_valid()
            return Response(serial.data, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'mensagem': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TesteViewQuery(generics.ListCreateAPIView):
    model = Teste
    serializer_class = TesteQuerySerializer

    def get_queryset(self):
        sql = """
                SELECT *, ate.descricao nome_estado  FROM AppTeste_municipio atm INNER JOIN AppTeste_estado ate ON ate.id  = atm.estado_id
              """

        queryset = Teste.objects.raw(sql)
        return queryset