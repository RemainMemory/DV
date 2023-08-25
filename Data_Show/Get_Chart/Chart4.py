import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar3D

# 读取CSV文件
df = pd.read_csv("./Data_csv/disposable_income_national.csv")

# 提取数据
years_quarters = df['年份_季度'].tolist()
income_wage = df['居民人均可支配工资性收入_累计值'].tolist()
income_business = df['居民人均可支配经营净收入_累计值'].tolist()
income_property = df['居民人均可支配财产净收入_累计值'].tolist()
income_transfer = df['居民人均可支配转移净收入_累计值'].tolist()


# 生成数据
def generate_data():
    data = []
    for i, yq in enumerate(years_quarters):
        stack_value = 0
        for j, income_type in enumerate([income_wage, income_business, income_property, income_transfer]):
            stack_value += income_type[i]
            data.append([i, j, stack_value])
        # 添加总收入项
        data.append([i, 4, stack_value])  # 4 是新添加的“总收入”项的y轴索引
    return data

# 创建3D柱状图
bar3d = Bar3D()
bar3d.add(
    "",
    generate_data(),
    shading="lambert",
    xaxis3d_opts=opts.Axis3DOpts(data=years_quarters, type_="category"),
    yaxis3d_opts=opts.Axis3DOpts(data=["工资收入", "经营收入", "财产收入", "转移收入", "总收入"], type_="category"),  # 添加了“总收入”
    zaxis3d_opts=opts.Axis3DOpts(type_="value"),
)
bar3d.set_global_opts(title_opts=opts.TitleOpts(title="居民人均可支配收入3D柱状图", pos_left="center"))
bar3d.set_series_opts(**{"stack": "stack"})
bar3d.render("income_bar3d_stacked.html")
