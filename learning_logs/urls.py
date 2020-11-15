"""定义learning_logs的URL模式"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # ?P<topic_id> 将匹配的值存储到topic_id 中； 而表达式\d+ 与包含在两个斜杆内的任何数字都匹配， 不管这个数字为多少位。
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
