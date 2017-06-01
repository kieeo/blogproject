from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^index$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
        # 这个归档视图对应的 URL 的正则表达式和 detail 视图函数对应的 URL 是类似的，
        # 这在之前我们讲过。两个括号括起来的地方是两个命名组参数，Django 会从用户访问的
        # URL 中自动提取这两个参数的值，然后传递给其对应的视图函数。例如如果用户想查看
        # 2017 年 3 月下的全部文章，他访问 /archives/2017/3/，
        # 那么 archives 视图函数的实际调用为：archives(request, year=2017, month=3)。
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),

]

