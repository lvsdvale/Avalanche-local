from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from Avalancheutfpr.models import *
from Blog.models import *

class EventosApiView(APIView):
    def get(self,request):
        Eventos = eventos.objects.all()
        serializer = EventosSerializer(Eventos, many=True)
        return Response(serializer.data)

