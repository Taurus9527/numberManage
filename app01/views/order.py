import random

from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app01.utils.bootstrap import BootStrapModelForm
from app01 import models
from app01.utils.pagination import Pagination




class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ["oid", "admin"]


def order_list(request):
    queryset = models.Order.objects.all().order_by("-id")
    page_object = Pagination(request, queryset)
    form = OrderModelForm()

    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }


    return render(request, 'order_list.html', context)

@csrf_exempt
def order_add(request):
    """ 新建订单 （Ajax请求）"""
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # 订单号：将一些额外的字段随机生成
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000,9999))

        # 固定设置管理员ID：当前登录系统管理员
        form.instance.admin_id = request.session["info"]["id"]
        form.save()
        return JsonResponse({"status": True})

    return JsonResponse({"status": False,  "error": form.errors})
