from rest_framework import serializers
from . models import TaskStage,AccountDetail,Label,Task,Attachment,Comment




class AccountDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model =  AccountDetail
        fields=['name','img']

class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Label
        fields=['label','color']



class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields=['name','size']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Comment
        fields=['name','message','date']


class TaskSerializer(serializers.ModelSerializer):
    members = AccountDetailSerializer(many=True)
    labels = LabelSerializer(many=True)
    comments = serializers.SerializerMethodField()
    attachments = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'


    def get_comments(self, obj):
        comments = Comment.objects.filter(task=obj)
        return CommentSerializer(comments, many=True).data

    def get_attachments(self, obj):
        attachments = Attachment.objects.filter(task=obj)
        return AttachmentSerializer(attachments, many=True).data

class TaskStageSerializer(serializers.ModelSerializer):
    tasks=serializers.SerializerMethodField()
    
    def get_tasks(self,obj):
        task=Task.objects.filter(task_stage=obj)
        return TaskSerializer(task,many=True).data

    class Meta:
        model =  TaskStage
        fields='__all__'

