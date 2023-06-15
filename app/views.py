from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from app.models import *
from rest_framework.response import Response
from app.serializers import * 

# Create your views here.


class Product_ViewSet(ViewSet):
    def list(self, request):

        PO=Product.objects.all()

        PSD=Product_Serializer(PO, many=True)

        return Response(PSD.data)
    def create(self, request):
        PSD=Product_Serializer(data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'Msg':'Data Is Inserted!!'})
        else:
            return Response({'Fail':'Not A Valid Data!!'}) 

    def retrieve(self, request, pk):
        PO=Product.objects.get(pk=pk)

        PSD=Product_Serializer(PO)
        return Response(PSD.data)

    def update(self, request, pk):
        PO=Product.objects.get(pk=pk)
        PSD=Product_Serializer(PO, data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'Msg':'Data Is Updated Successfully!!'})
        else:
            return Response({'Fail':'Data Is Not Valid!!'}) 

    def partial_update(self, request, pk):
        PO=Product.objects.get(pk=pk)
        PSD=Product_Serializer(PO, data=request.data, partial=True)
        if PSD.is_valid():
            PSD.save()
            return Response({'Msg':'Data Is Updated Successfully!!'})
        else:
            return Response({'Fail':'Data Is Not Valid!!'}) 

    def destroy(self, request, pk):
       Product.objects.get(pk=pk).delete()
        
       return Response({'Msg':'Data Is Deleted!!'})    
        


            

    