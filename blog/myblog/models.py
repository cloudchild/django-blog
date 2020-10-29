from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 文章分类
class Category(models.Model):
    name = models.CharField('分类',max_length=100)
    index = models.IntegerField(default=999,verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章标签
class Tag(models.Model):
    name = models.CharField('标签',max_length = 100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章内容
class Article(models.Model):
    # 标题
    title = models.CharField('标题',max_length=70)
    # 摘要
    excerpt = models.TextField('摘要',max_length=200, blank=True)
    # 分类 分类与分类表一对多的关系
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类',blank=True, null=True)
    # 标签 标签与标签表多对多的关系
    tags = models.ManyToManyField(Tag,verbose_name='标签',blank=True)
    # 内容
    content = models.TextField()
    # 作者 通过ForeignKey 把文章和User 关联，一对一
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    # 浏览数
    views = models.PositiveIntegerField('浏览量',default=0)
    # 发布时间
    created_time = models.DateTimeField('发布时间',auto_now_add=True)
    # 修改时间
    modified_time = models.DateTimeField('修改时间',auto_now=True)
    # 封面图片
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
# 幻灯图
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'
# 推荐位
class Recommended(models.Model):
    name = models.CharField('推荐位',max_length = 100)

    class Meta:
        verbose_name = '推荐'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
# 友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网站',max_length=100)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name