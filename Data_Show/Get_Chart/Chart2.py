import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Timeline, Pie


# 读取CSV并格式化
def generate_Chart2():
    def read_csv_and_format(filename="./Data_csv/disposable_income_national.csv"):
        df = pd.read_csv(filename)
        data = {}
        for index, row in df.iterrows():
            year_quarter = row['年份_季度']
            data[year_quarter] = [{"name": col, "value": row[col]} for col in df.columns[1:]]
        return data

    # 获取年度_季度饼图
    def get_year_quarter_pie_chart(year_quarter: str):
        year_quarter_data = total_data[year_quarter]
        names = [x["name"] for x in year_quarter_data]
        values = [x["value"] for x in year_quarter_data]

        pie = (
            Pie()
            .add(
                series_name="",
                data_pair=[list(z) for z in zip(names, values)],
                radius=["20%", "40%"],
                label_opts=opts.LabelOpts(
                    position="outside",
                    formatter="{b}: {c}"
                )
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Total residents' pension disposable income",
                                          subtitle="数据来自相关统计局", pos_left="center"),
                legend_opts=opts.LegendOpts(type_="scroll", pos_left="75%", orient="vertical", pos_top="10%"),
            )
        )
        return pie

    # 总数据
    total_data = read_csv_and_format()

    timeline_pie = Timeline(init_opts=opts.InitOpts(width="1000px", height="600px"))

    # 生成饼图
    for year_quarter in sorted(total_data.keys()):  # 根据你的数据范围调整年份和季度
        pie = get_year_quarter_pie_chart(year_quarter)
        timeline_pie.add(pie, time_point=year_quarter)

    timeline_pie.add_schema(
        is_auto_play=True,
        play_interval=1000,
        orient="horizontal",
        pos_left="10",
        pos_right="10",
        pos_bottom="10",
    )

    timeline_pie.render("disposable_income_by_year_quarter_pie.html")
