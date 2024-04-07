from django.urls import path,include
from . views import UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)








urlpatterns = [
    
    path('tokenobtainpair/',TokenObtainPairView.as_view(),name='tokenobatain'),
    path('tokenrefresh/',TokenRefreshView.as_view(),name='tokenrefresh'),
    path('tokenverify/',TokenVerifyView.as_view(),name='tokenverify'),
    path('user/', UserView.as_view({'get':'list','post':'create'}),name="user"),
    # path('user',signup_view,name='signup'),

]