from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.bootstrap import BootStrapModelForm
from django import forms



class UserModelForm(BootStrapModelForm):
    name = forms.CharField(
        min_length=3,
        label='用户名',
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]

class PrettyModelForm(BootStrapModelForm):
    # 方式1验证
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1\d{10}$', "手机号必须1开头")],
    )

    class Meta:
        model = models.PrettyNum
        # fields = "__all__"
        fields = ["mobile", "price", "level", "status"]
        # exclude = ['level']


    # 验证方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()

        if exists:
            raise ValidationError("手机号已存在!!!")
        return txt_mobile

class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True, label="手机号")
    # 方式1验证
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1\d{10}$', "手机号必须1开头")],
    )

    class Meta:
        model = models.PrettyNum
        # fields = "__all__"
        fields = ["mobile", "price", "level", "status"]
        # exclude = ['level']

    # 验证方式2
    def clean_mobile(self):
        # 当前编辑的ID
        # self.instance.pk

        txt_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在!!!")
        return txt_mobile