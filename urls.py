"""
URL configuration for bgn_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from learn.views import *
from django.urls.conf import include
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

#from django.views.generic.base import TemplateView
urlpatterns = [
    path('',learn,name="learn"),
    #path('login/',learn,name="learn"),
    #path('learn/',learn,name="learn"),
    #path('',user_login,name="index"),
    path('register/',register,name="register"),
    path('admi/',admi,name="admi"),
    path('image/',img,name="img"),
    path('admin/', admin.site.urls),
    path('user_login/',user_login,name="user_login"),
    path('user_details/', user_details, name='user_details'),
    path('user_details/', user_details, name='user_details'),
    path('delete/', delete, name='delete'),
    path('payment/',pay,name="pay"),
    path('add_money/',add_money,name="add_money"),
    path('transaction-history/', transaction_history, name='transaction_history'),
   

   # path('', TemplateView.as_view(template_name='home.html'),name='user_details' ), 
      

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
