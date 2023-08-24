"""Data_Show URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Data_Show.chart.demo_Bar import *
from Data_Show.splider.spilderCount import splider_Request
urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置访问demo01的url地址
    path('bar01/', bar01),
    path('spliderRequest/', splider_Request),
]
