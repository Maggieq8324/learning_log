"""为应用程序users定义URL模式"""

from django.urls import path, re_path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # 登录页面,LoginView.as_view-验证登录的视图类
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注销
    path('logout/', views.logout_view, name='logout'),
    # 注册
    path('register/', views.register, name='register')
]
