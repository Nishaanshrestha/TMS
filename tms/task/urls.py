


from django.urls import path,include
from . views import Attachment_view,Label_view,Comment_view,Task_view,Taskstage_view,Accountdetail_view
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('attachment',Attachment_view,basename='attachment')
router.register('label',Label_view,basename='label')
router.register('comments',Comment_view,basename='comments')
router.register('taskview',Task_view,basename='taskview')
router.register('taskstage',Taskstage_view,basename='taskstage')
router.register('accountdetail',Accountdetail_view,basename='accountdetail')


urlpatterns = [
    path('',include(router.urls)),
]