from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# POST method
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg': 'This is POST request'})

# GET and POST both together if request come from GET it show GET else POST.
@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        return Response({'msg': 'This is GET request'})
    if request.method == "POST":
        print(request.data)
        return Response({'msg': 'This is POST request', 'data': request.data})