# 导入图表库，* 匹配所有图表
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
import csv
import json
import pymysql
# 基本柱状图
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
import csv


def read_csv(filename):
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the first line (header)
            for row in csvreader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


def bar01():
    # 获取数据
    data = read_csv("./Data_csv/disposable_income_national.csv")

    if len(data) > 0:
        x_data = [item[0] for item in data]  # Assuming the first column contains the x-axis labels
        y1_data = [float(item[2]) for item in data]  # Assuming the third column contains data for y1_axis
        y2_data = [float(item[3]) for item in data]  # Assuming the fourth column contains data for y2_axis
        y3_data = [float(item[4]) for item in data]  # Assuming the fifth column contains data for y3_axis
        y4_data = [float(item[5]) for item in data]  # Assuming the sixth column contains data for y4_axis

        bar = (
            Bar()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name="居民人均可支配工资性收入_累计值", y_axis=y1_data,
                       label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="居民人均可支配经营净收入_累计值", y_axis=y2_data,
                       label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="居民人均可支配财产净收入_累计值", y_axis=y3_data,
                       label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="居民人均可支配转移净收入_累计值", y_axis=y4_data,
                       label_opts=opts.LabelOpts(is_show=False))
            .extend_axis(
                yaxis=opts.AxisOpts(
                    name="元",
                    type_="value",
                    min_=0,
                    max_=40000,
                    interval=5000,
                    axislabel_opts=opts.LabelOpts(formatter="{value}￥"),
                )
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Disposable income national", subtitle="数据来自相关统计局",
                                          pos_left="center"),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                toolbox_opts=opts.ToolboxOpts(is_show=True, orient="vertical", pos_left="left", pos_top="center"),
                legend_opts=opts.LegendOpts(pos_bottom="0%")  # 将图例放在图的最下方
            )

        )

        line = (
            Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
                series_name="居民人均可支配收入_累计值",
                yaxis_index=1,
                y_axis=[float(item[1]) for item in data],  # Assuming the second column contains the data
                label_opts=opts.LabelOpts(is_show=False),

            )
        )

        bar.overlap(line).render("mixed_bar_and_line.html")
    else:
        print("没有查询到数据")


if __name__ == "__main__":
    bar01()
