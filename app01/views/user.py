from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm



def user_list(request):
    """用户管理"""

    # 获取所有用户列表
    queryset = models.UserInfo.objects.all()

    page_object = Pagination(request, queryset, page_size=2)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
    }

    return render(request, 'user_list.html', context)


def user_add(request):
    """添加用户"""
    if request.method == "GET":
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all(),
        }
        return render(request, 'user_add.html', context)

    # 获取用户提交的数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender_id = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    # 添加到数据库中
    models.UserInfo.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=ctime,
                                   gender=gender_id, depart_id=depart_id)

    # 返回到用户列表中
    return redirect("/user/list/")


def user_model_form_add(request):
    """添加用户：ModelForm版本"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})

    # 用户post提交数据，数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list/')

    # 校验失败（页面显示错误信息）
    return render(request, 'user_model_form_add.html', {"form": form})


def user_edit(request, nid):
    """编辑用户"""
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据（对象）
        form = UserModelForm(instance=row_object)
        return render(request, "user_edit.html", {"form": form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存用户输入的所有数据，只修改某个字段的值form.instance.字段名 = 值
        form.save()
        return redirect('/user/list/')
    return render(request, "user_edit.html", {"form": form})


def user_delete(request, nid):
    """删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')