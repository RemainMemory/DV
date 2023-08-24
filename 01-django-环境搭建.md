



# django 环境搭建

## 1 django介绍

​       Django 是使用 Python 语言开发的一款免费而且开源的 Web 应用框架。由于 Python 语言的跨平台性，所以 Django 同样支持 Windows、Linux 和 Mac 系统。

​       在 Python 语言炽手可热的当下，Django 也迅速的崛起，在 Web 开发领域占有一席之地。基于 Python 开发的框架除了 Django 外，还有可以实现快速建站 Flask 和支持高并发处理的 Tornado ，而 Django 是最有代表性的一位，它们三者是当前最流行的 Python Web 框架



## 2 django安装与配置教程

 

不同 Django 版本对 Python 版本的要求也是不一样的 ，Django 对 Python 版本的支持，如表格所示：



| Django版本  | Python版本                |
| --------- | ----------------------- |
| 1.8       | 2.7, 3.2, 3.3, 3.4, 3.5 |
| 1.9, 1.10 | 2.7, 3.4, 3.5           |
| 1.11x     | 2.7, 3.4, 3.5, 3.6      |
| 2.0       | 3.4, 3.5, 3.6, 3.7      |
| 2.1, 2.2  | 3.5, 3.6, 3.7           |
| 3.0       | 3.6, 3.7, 3.8           |



安装步骤如下：

一： 安装django

　　这里只介绍较为简单的pip命令安装方式。

　　win+r，调出cmd，运行命令：pip install django==2.0.2

二：配置环境变量





## 3 django 创建项目

1 创建项目

```
django-admin.py startproject HelloWorld
```

或者

```
django-admin.py startproject HelloWorld
```

2：启动服务器

```
python manage.py runserver localhost:8000 
```



3 打开 setting.py文件里，设置静态页面代码配置，代码如下：

```python
STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"static"),
)
```

4 注释setting.py第46行代码，代码如下：，

```
# 'django.middleware.csrf.CsrfViewMiddleware',
```








