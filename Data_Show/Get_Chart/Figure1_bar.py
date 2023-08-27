import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Timeline, Bar

# 读取CSV并格式化
def read_csv_and_format(filename="./Data_csv/disposable_income_by_province.csv"):
    df = pd.read_csv(filename)
    data = {}
    for index, row in df.iterrows():
        year = int(row['年份'])
        data[year] = [{"name": name, "value": value} for name, value in zip(name_list, list(row[1:]))]
    return data

# 年度数据格式化
def format_year_data(year_data):
    sorted_data = sorted(year_data, key=lambda x: x['value'], reverse=True)
    return sorted_data


# 地区列表
name_list = ["全国", "上海市", "云南省", "内蒙古自治区", "北京市", "吉林省", "四川省", "天津市", "宁夏回族自治区",
             "安徽省", "山东省", "山西省", "广东省", "新疆维吾尔自治区", "江苏省", "江西省", "河北省", "河南省",
             "浙江省", "海南省", "湖北省", "湖南省", "甘肃省", "福建省", "贵州省", "辽宁省", "重庆市", "陕西省",
             "青海省", "黑龙江省", "广西壮族自治区", "西藏自治区"]

# 总数据
total_data = {}
total_data["dataIncome"] = read_csv_and_format()

timeline_bar = Timeline(init_opts=opts.InitOpts(width="1000px", height="600px"))

# 生成柱状图
for y in range(2014, 2022):  # 根据你的数据范围调整年份
    sorted_year_data = format_year_data(total_data["dataIncome"][y])
    names = [x["name"] for x in sorted_year_data]
    values = [x["value"] for x in sorted_year_data]

    bar = (
        Bar(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add_xaxis(xaxis_data=names)
        .add_yaxis(
            series_name="人均可支配收入",
            y_axis=values,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="{}全国及各省份居民人均可支配收入".format(y), subtitle="数据来自相关统计局"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            toolbox_opts=opts.ToolboxOpts(is_show=True, orient="vertical", pos_left="left", pos_top="center")
        )
    )

    timeline_bar.add(bar, time_point=str(y))

timeline_bar.render("disposable_income_by_province_bar.html")
