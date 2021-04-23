from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import product

# Create your views here.
"""@api_view(['GET'])
def apioverview(req):
	api_urls={
	'List':'/product-list',
	'Detailview':'/product-detail/<int:id>',
	'Create':'/product-create/',
	'Update':'/product-update/<int:id>',
	'Delete':'/product-delete/<int:id>',
	}
	return Response(api_urls)
"""
@api_view(['GET'])
def Showall(req):
	products=product.objects.all()
	serializer=ProductSerializer(products,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(req,pk):
	products=product.objects.get(id=pk)
	serializer=ProductSerializer(products,many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(req):
	serializer=ProductSerializer(data=req.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(req,pk):
	products=product.objects.get(id=pk)
	serializer=ProductSerializer(instance=products,data=req.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(req,pk):
	products=product.objects.get(id=pk)
	products.delete()
	return Response("successfuly deleted")

