from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
    path('index/', views.index, name='index'),  # 网站首页
    path('list/<int:lid>/', views.list, name='list'),  # 列表页
    path('show-<int:sid>.html', views.show, name='show'),  # 内容页
    path('tag/<tag>', views.tag, name='tags'),  # 标签列表页
    path('s/', views.search, name='search'),  # 搜索列表页
    path('about/', views.about, name='about'),  # 联系我们单页
]