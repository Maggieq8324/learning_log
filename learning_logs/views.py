from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    """学习笔记的主页"""
    """render根据视图提供的数据响应渲染"""
    return render(request, 'learning_logs/index.html')


@login_required()
def topics(request):
    """学习笔记的主题"""
    content = {'topics': Topic.objects.filter(owner=request.user).order_by('date_added')}
    return render(request, 'learning_logs/topics.html', content)


@login_required()
def topic(request, topic_id):
    """显示单个主题及其所有条目"""
    topic_item = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic_item.owner != request.user:
        raise Http404
    entries = topic_item.entry_set.order_by('-date_added')
    content = {'topic': topic_item, 'entries': entries}
    return render(request, 'learning_logs/topic.html', content)


@login_required()
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据，添加新表单
        form = TopicForm()
    else:
        # 对POST提交的数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic_item = form.save(commit=False)
            new_topic_item.owner = request.user
            new_topic_item.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    content = {'form': form}
    return render(request, 'learning_logs/new_topic.html', content)


@login_required()
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic_item = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据，添加新表单
        form = EntryForm()
    else:
        # 对POST提交的数据进行处理
        form = EntryForm(data=request.POST)
        print(form)
        if form.is_valid():
            entry_item = form.save(commit=False)
            entry_item.topic = topic_item
            entry_item.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    content = {'topic': topic_item, 'form': form}
    return render(request, 'learning_logs/new_entry.html', content)


@login_required()
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry_item = Entry.objects.get(id=entry_id)
    topic_item = entry_item.topic

    if topic_item.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # instance=entry_item 创建一个表单，并使用对象中的信息填充
        form = EntryForm(instance=entry_item)
    else:
        # instance=entry_item, data=request.POST 根据对象创建表单，并根据POST中的数据进行修改
        form = EntryForm(instance=entry_item, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_item.id]))

    context = {'entry': entry_item, 'topic': topic_item, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
