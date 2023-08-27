import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Timeline, Pie

# 读取CSV并格式化
def read_csv_and_format(filename="./Data_csv/disposable_income_by_province.csv"):
    df = pd.read_csv(filename)
    data = {}
    for index, row in df.iterrows():
        year = int(row['年份'])
        data[year] = [{"name": name, "value": value} for name, value in zip(name_list, list(row[1:]))]
    return data

# 获取大区数据
def get_area_data(year_data):
    area_values = {key: 0 for key in area_dict.keys()}  # 初始化所有大区的值为0
    for item in year_data:
        for area, provinces in area_dict.items():
            if item["name"][:-1] in provinces:  # 截取字符串去掉最后的 "省" 或 "市"
                area_values[area] += item["value"]
    return [{"name": area, "value": value} for area, value in area_values.items()]


# 地区列表
name_list = ["全国", "上海市", "云南省", "内蒙古自治区", "北京市", "吉林省", "四川省", "天津市", "宁夏回族自治区",
             "安徽省", "山东省", "山西省", "广东省", "新疆维吾尔自治区", "江苏省", "江西省", "河北省", "河南省",
             "浙江省", "海南省", "湖北省", "湖南省", "甘肃省", "福建省", "贵州省", "辽宁省", "重庆市", "陕西省",
             "青海省", "黑龙江省", "广西壮族自治区", "西藏自治区"]

# 大区字典
area_dict = {
    "华东": ["江苏", "浙江", "山东", "安徽", "江西", "福建", "上海"],
    "华南": ["广东", "广西", "海南"],
    "华中": ["湖北", "湖南", "河南"],
    "华北": ["山西", "河北", "内蒙古", "北京", "天津"],
    "东北": ["吉林", "辽宁", "黑龙江"],
    "西北": ["新疆", "陕西", "甘肃", "宁夏", "青海"],
    "西南": ["四川", "西藏", "贵州", "云南", "重庆"]
}

# 总数据
total_data = {}
total_data["dataIncome"] = read_csv_and_format()

timeline_pie = Timeline(init_opts=opts.InitOpts(width="1000px", height="600px"))

# 生成饼图
for y in range(2014, 2022):  # 根据你的数据范围调整年份
    sorted_year_data = get_area_data(total_data["dataIncome"][y])
    names = [x["name"] for x in sorted_year_data]
    values = [x["value"] for x in sorted_year_data]

    pie = (
        Pie()
        .add(
            series_name="",
            data_pair=[list(z) for z in zip(names, values)],
            radius=["20%", "40%"],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="{}年按大区分类的收入分布".format(y)),
        )
    )

    timeline_pie.add(pie, time_point=str(y))

timeline_pie.render("disposable_income_by_province_pie.html")
