from django.shortcuts import render
from rest_framework .permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework . authentication import SessionAuthentication
from . models import Task,Attachment,Comment,TaskStage,AccountDetail,Label
from . serializers import AttachmentSerializer,TaskSerializer,CommentSerializer,TaskStageSerializer,AccountDetailSerializer,LabelSerializer
from rest_framework import viewsets

class Task_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class Attachment_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

class Comment_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class Taskstage_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    queryset = TaskStage.objects.all()
    serializer_class = TaskStageSerializer

class Accountdetail_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    queryset = AccountDetail.objects.all()
    serializer_class = AccountDetailSerializer

class Label_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    queryset = Label.objects.all()
    serializer_class = LabelSerializer