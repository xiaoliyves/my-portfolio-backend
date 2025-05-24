from django.shortcuts import render

from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all().order_by("-id")
    #Django 中 ORM（資料庫查詢語法）的寫法，用來從資料庫中取得 Project 模型的資料，並依照 id 倒序排列。
    serializer_class = ProjectSerializer
