import json

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
from Data_Show.views import JsonResponse
from django.shortcuts import HttpResponse


# 创建柱状图
# 基本柱状图
def bar01(request):
    # 柱状图数据格式
    x = ["2010", "2011", "2012", "2013", "2014", "2015"]
    y = [11.9, 12.0, 13.1, 11.9, 12.0, 13.1]
    # 第一步：创建图表对象 (柱状图)
    bar = Bar()
    # 添加x轴数据
    bar.add_xaxis(x)
    # 添加y轴数据
    bar.add_yaxis("统计人口出生率", y, bar_width=20, color="red")
    # 设置全局配置项
    data = bar.dump_options_with_quotes()
    return JsonResponse(json.loads(data))


# 排名图
def bar02():
    x = ["2010", "2011", "2012", "2013", "2014", "2015"]
    y = [11.9, 12.0, 13.1, 11.9, 12.0, 13.1]
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", y)
        .add_yaxis("商家B", y)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-翻转 XY 轴"))
        .render("bar_reversal_axis.html")
    )


if __name__ == "__main__":
    bar02()
