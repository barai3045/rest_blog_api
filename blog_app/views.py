from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blog
from .serializer import BlogSerializer



@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method =="GET":
        all_blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(all_blogs, many=True)
        return Response(serializer.data)

    if request.method =="POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, pk):
    if request.method == "GET":
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        
        return Response(serializer.data)
    if request.method =="PUT":
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        
    if request.method =="DELETE":
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response()