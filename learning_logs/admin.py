from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry
# 让Django通过管理网址管理模型
admin.site.register(Topic)
admin.site.register(Entry)
