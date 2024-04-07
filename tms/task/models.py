from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()



# Create your models here.
class TaskStage(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class AccountDetail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    img = models.URLField(max_length=200)
    def __str__(self):
        return self.name


class Label(models.Model):
    label = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.label
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cover = models.URLField(max_length=200, null=True)
    members = models.ManyToManyField(AccountDetail, related_name='member')
    labels = models.ManyToManyField(Label, related_name='task_label')
    due_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        help_text="Enter a due date in the future.",
        null=True,
    )
    task_stage = models.ForeignKey(TaskStage, on_delete=models.CASCADE)
    created_date=models.DateField(auto_now=True,null=True)
    assigned_to=models.ManyToManyField(User,related_name='assgined_to')
    assigned_by=models.ForeignKey(User, related_name='assigned_by', on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name
    
class Attachment(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField("image", upload_to='attachment/', null=True, blank=True)
    size = models.CharField(max_length=50)
    task=models.ForeignKey(Task, related_name="attachment" ,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    src = models.URLField(max_length=200)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    task=models.ForeignKey(Task, related_name="comment" ,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
    

    



