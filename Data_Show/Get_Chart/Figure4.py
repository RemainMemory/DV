import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Tree, Timeline


# 从CSV文件中读取数据
def read_csv_and_format(filename="./Data_csv/disposable_income_by_province.csv"):
    df = pd.read_csv(filename)
    data = {}
    for index, row in df.iterrows():
        year = int(row['年份'])
        data[year] = [{"name": name, "value": value} for name, value in zip(name_list, list(row[1:]))]
    return data


# 将数据转换为树形结构
# 将数据转换为树形结构
def convert_to_tree_structure(year_data, area_dict):
    tree_data = []
    for area, provinces in area_dict.items():
        children = []
        for item in year_data:
            # 去掉省份名称最后的“省”、“市”、“自治区”等
            short_name = (item["name"].replace("省", "").replace("市", "").replace("自治区", "").
                          replace("壮族", "").replace("维吾尔", "").replace("回族", ""))
            if short_name in provinces:
                children.append({"name": f"{item['name']} ({item['value']})"})
        tree_data.append({"name": area, "children": children})
    return [{"name": "全国", "children": tree_data}]



# 地区列表和大区字典（与之前相同）
name_list = ["全国", "上海市", "云南省", "内蒙古自治区", "北京市", "吉林省", "四川省", "天津市", "宁夏回族自治区",
             "安徽省", "山东省", "山西省", "广东省", "新疆维吾尔自治区", "江苏省", "江西省", "河北省", "河南省",
             "浙江省", "海南省", "湖北省", "湖南省", "甘肃省", "福建省", "贵州省", "辽宁省", "重庆市", "陕西省",
             "青海省", "黑龙江省", "广西壮族自治区", "西藏自治区"]

area_dict = {
    "华东": ["江苏", "浙江", "山东", "安徽", "江西", "福建", "上海"],
    "华南": ["广东", "广西", "海南"],
    "华中": ["湖北", "湖南", "河南"],
    "华北": ["山西", "河北", "内蒙古", "北京", "天津"],
    "东北": ["吉林", "辽宁", "黑龙江"],
    "西北": ["新疆", "陕西", "甘肃", "宁夏", "青海"],
    "西南": ["四川", "西藏", "贵州", "云南", "重庆"]
    # ...（其他大区）
}

# 读取CSV数据
total_data = read_csv_and_format()

# 创建时间轴对象
timeline = Timeline(init_opts=opts.InitOpts(width="1200px", height="800px"))

# 生成树形图并添加到时间轴
for y in range(2014, 2022):  # 根据你的数据范围调整年份
    year_data = total_data[y]
    tree_data = convert_to_tree_structure(year_data, area_dict)

    tree = (
        Tree()
        .add("", tree_data, collapse_interval=2)
        .set_global_opts(title_opts=opts.TitleOpts(title=f"Tree for Year {y}"))
    )
    timeline.add(tree, f"{y}年")

# 渲染到HTML文件
timeline.render("tree_timeline.html")
