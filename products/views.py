from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
# from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from .pagination import ProductPagination
import razorpay
import os

class ProductsViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    parser_classes = (MultiPartParser, FormParser)

class OrdersViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        client = razorpay.Client(auth=(os.environ.get("RAZORPAY_API_KEY"), os.environ.get("RAZORPAY_SECRET_KEY")))
        client.set_app_details({"title" : "Mobile Shop", "version" : "v1.0.0"})