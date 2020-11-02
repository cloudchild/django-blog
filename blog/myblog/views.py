from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

# 首页
def index(request):

    # 添加数据，实例化表类，在实例化里传参为字段和值
    obj = models.Article(title='增加标题二', category_id=4, content='增加内容二', author_id=1)
    # 写入数据库
    obj.save()
    # 第三种方法：将要写入的数据组合成字典，键为字段值为数据
    dic = {'title': '增加标题三', 'category_id': '4', 'content': '增加内容三', 'author_id': '1'}
    # 添加到数据库，注意字典变量名称一定要加**
    models.Article.objects.create(**dic)
    # context定义了需要传递给模板的上下文
    context = {

        'obj': obj,
        'dic': dic,
    }
    #  render函数。它的作用是结合模板和上下文，并返回渲染后的HttpResponse对象。通俗的讲就是把context的内容，加载进模板，并通过浏览器呈现。
    return render(request,'index.html',context)
