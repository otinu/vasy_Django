
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

import products.scraping.cookpad as cookpad
import products.scraping.kurashiru as kurashiru
import products.scraping.cookpad as cookpad

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Kurashiru_ApiView(APIView):

    def get(self, request, format=None):
        return Response(kurashiru.Allread())

class Cookpad_ApiView(APIView):

    def get(self, request, format=None):
        return Response(cookpad.Allread())