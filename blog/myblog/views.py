from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category,Tag,Recommended
# Create your views here.

#首页
def index(request):
    allcategory = Category.objects.all()  # 通过Category表查出所有分类
    tags = Tag.objects.all()              # 热门标签
    # tui = Article.objects.filter(tui__id=1)[:3]  # 查询推荐位ID为1的文章
    allarticle = Article.objects.all().order_by('-id')[0:10]
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧标签
    # 把查询出来的分类封装到上下文里
    context = {
        'allcategory': allcategory,
        'tags':tags,
        # 'tui':tui,
        'allarticle':allarticle,
        'remen':remen,

    }
    return render(request, 'myblog/index.html', context)  # 把上下文传到index.html页面

#列表页
def list(request,lid):
    list = Article.objects.filter(category_id=lid)  # 获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)  # 获取当前文章的栏目名
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧的热门推荐
    allcategory = Category.objects.all()  # 导航所有分类
    tags = Tag.objects.all()  # 右侧所有文章标签
    return render(request, 'myblog/list.html', locals())
#内容页
def show(request,sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()  # 导航上的分类
    tags = Tag.objects.all()  # 右侧所有标签
    remen = Article.objects.filter(Recommended__id=2)[:6]  # 右侧热门推荐
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'myblog/show.html', locals())

#标签页
def tag(request, tag):
    pass

# 搜索页
def search(request):
    pass
# 关于我们
def about(request):
    pass