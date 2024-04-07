from django.contrib import admin
from . models import Task,Label,AccountDetail,Attachment,TaskStage,Comment

# Register your models here.
admin .site . register(Task),
admin .site . register(TaskStage),
admin .site . register(AccountDetail),
admin .site . register(Label),
admin .site . register(Attachment),
admin .site . register(Comment),

