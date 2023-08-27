import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline


# 读取CSV并格式化
def read_csv_and_format(filename="./Data_csv/disposable_income_by_province.csv"):
    df = pd.read_csv(filename)
    data = {}
    for index, row in df.iterrows():
        year = int(row['年份'])
        data[year] = [{"name": name, "value": value} for name, value in zip(name_list, list(row[1:]))]
    return data


# 地区列表
name_list = ["全国", "上海市", "云南省", "内蒙古自治区", "北京市", "吉林省", "四川省", "天津市", "宁夏回族自治区",
             "安徽省", "山东省", "山西省", "广东省", "新疆维吾尔自治区", "江苏省", "江西省", "河北省", "河南省",
             "浙江省", "海南省", "湖北省", "湖南省", "甘肃省", "福建省", "贵州省", "辽宁省", "重庆市", "陕西省",
             "青海省", "黑龙江省", "广西壮族自治区", "西藏自治区"]

# 总数据
total_data = {}
total_data["dataIncome"] = read_csv_and_format()

# 创建时间轴对象
timeline = Timeline(init_opts=opts.InitOpts(width="1000px", height="600px"))

# 添加地图到时间轴
for y in range(2014, 2022):  # 根据你的数据范围调整年份
    sorted_year_data = total_data["dataIncome"][y]
    names = [x["name"] for x in sorted_year_data]
    values = [x["value"] for x in sorted_year_data]

    map_ = (
        Map()
        .add(
            series_name="",
            data_pair=[list(z) for z in zip(names, values)],
            maptype="china",
            is_map_symbol_show=False,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="{}年全国各省份居民人均可支配收入".format(y),
                                      subtitle="数据来自相关统计局"),
            visualmap_opts=opts.VisualMapOpts(
                max_=100000,
                is_piecewise=True,
                pieces=[
                    # 5000一个区间
                    {"min": 100000, "max": 1000000, "label": "100,000-1,000,000"},
                    {"min": 80000, "max": 100000, "label": "80,000-100,000"},
                    {"min": 75000, "max": 79999, "label": "75,000-79,999"},
                    {"min": 70000, "max": 74999, "label": "70,000-74,999"},
                    {"min": 65000, "max": 69999, "label": "65,000-69,999"},
                    {"min": 60000, "max": 64999, "label": "60,000-64,999"},
                    {"min": 55000, "max": 59999, "label": "55,000-59,999"},
                    {"min": 50000, "max": 54999, "label": "50,000-54,999"},
                    {"min": 45000, "max": 49999, "label": "45,000-49,999"},
                    {"min": 40000, "max": 44999, "label": "40,000-44,999"},
                    {"min": 35000, "max": 39999, "label": "35,000-39,999"},
                    {"min": 30000, "max": 34999, "label": "30,000-34,999"},
                    {"min": 25000, "max": 29999, "label": "25,000-29,999"},
                    {"min": 20000, "max": 24999, "label": "20,000-24,999"},
                    {"min": 15000, "max": 19999, "label": "15，000-19,999"},
                    {"min": 10000, "max": 14999, "label": "10,000-14,999"},
                    {"min": 5000, "max": 9999, "label": "5,000-9,999"},
                    {"min": 0, "max": 4999, "label": "0-4,999"}
                ]
            ),
        )
    )
    timeline.add(map_, "{}年".format(y))

# 渲染到HTML文件
timeline.render("disposable_income_by_province_timeline.html")
