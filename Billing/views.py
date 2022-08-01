from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .Serializer import ItemSerializer
from .models import Item


# Create your views here.
class ItemView(APIView):
    def get(self,request):
        queryset = Item.objects.all()
        category = self.request.GET.get('category', None)
        subcategory = self.request.GET.get('subcategory', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        if subcategory is not None:
            queryset = queryset.filter(subcategory=subcategory)
        itemSerializer = ItemSerializer(queryset, many=True)

        return Response(itemSerializer.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        category = request.data.get('category', None)
        subcategory = request.data.get('subcategory', None)

        if Item.objects.filter(name=request.data.get('name'), category=category, subcategory=subcategory).exists():
            return Response({'Error': 'Item Already Added'}, status=status.HTTP_400_BAD_REQUEST)
        itemSerializer = ItemSerializer(data=request.data)
        if itemSerializer.is_valid():
            itemSerializer.save()
            return Response(itemSerializer.data, status=status.HTTP_201_CREATED)
        return Response(itemSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        category = request.data.get('category', None)
        subcategory = request.data.get('subcategory', None)
        if not Item.objects.filter(name=request.data.get('name'), category=category, subcategory=subcategory).exists():
            return Response({'Error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        item = Item.objects.get(name=request.data.get('name'), category=category, subcategory=subcategory)
        itemSerializer = ItemSerializer(instance=item,data=request.data)
        if itemSerializer.is_valid():
            itemSerializer.save()
            return Response(itemSerializer.data, status=status.HTTP_201_CREATED)
        return Response(itemSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        category = request.data.get('category', None)
        subcategory = request.data.get('subcategory', None)
        if not Item.objects.filter(name=request.data.get('name'), category=category, subcategory=subcategory).exists():
            return Response({'Error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        item = Item.objects.get(name=request.data.get('name'), category=category, subcategory=subcategory)

        item.delete()
        return Response({'Message':'Item Deleted'},status=status.HTTP_202_ACCEPTED)

