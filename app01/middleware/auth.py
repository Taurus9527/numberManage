from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    """ 中间件 1 """

    def process_request(self, request):

        # 0.排除那些不需要登录就能访问的页面，eg. /login/
        if request.path_info in ["/login/", "/image/code/"]:
            return

        # 1.读取当前访问用户的session信息，如果能读到，说明已经登陆过，就可以继续往后走。
        info_dict = request.session.get("info")
        if info_dict:
            return

        # 2.没有登陆过，重新回到登陆界面
        return redirect('/login/')


