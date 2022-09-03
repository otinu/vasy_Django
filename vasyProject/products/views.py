"""
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
"""
import scraping.cookpad as cookpad
import scraping.kurashiru as kurashiru

print(cookpad.read())
print(kurashiru.read())
"""
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class NonModel_ApiView(APIView):

    def get(self, request, format=None):
        # ダミーデータを返却
        
        # return  Response({"APIより": "vasyProjectのviewsからやってきました！！"})
        return Response(cookpad.read())

"""