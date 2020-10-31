from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

# 首页
def index(request):
    # 对Article进行声明并实例化，然后生成对象allarticle
    allarticle = Article.objects.all()
    # 新加一个列表
    list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    # context定义了需要传递给模板的上下文
    context = {
        'allarticle': allarticle,
        'list':list,
    }
    #  render函数。它的作用是结合模板和上下文，并返回渲染后的HttpResponse对象。通俗的讲就是把context的内容，加载进模板，并通过浏览器呈现。
    return render(request,'index.html',context)
