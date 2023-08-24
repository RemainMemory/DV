from Data_Show.splider.demo03 import splider
from Data_Show.views import JsonResponse
from django.shortcuts import HttpResponse
import json


# 定义访问函数
def splider_Request(request):
    rs = splider(request)
    info = {"data": rs}
    return HttpResponse(json.dumps(info), content_type="application/json")