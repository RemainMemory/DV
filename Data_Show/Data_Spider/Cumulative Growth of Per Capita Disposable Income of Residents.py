import requests
import time
import urllib3
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetch_data(url, search_query, year, quarters=None):
    data_dict = {}
    parameters = {
        "s": f"{year}{search_query}",
        "m": "searchdata",
        "db": "",
        "p": "0"
    }
    # time.sleep(1)
    try:
        response = requests.get(url, params=parameters, verify=False)
        response.raise_for_status()
        data = response.json()

        if quarters and any(province in search_query for province in ["云南省", "贵州省", "四川省",
                                                                      "广西壮族自治区", "重庆市", "西藏自治区",
                                                                      "陕西省", "甘肃省", "青海省", "宁夏回族自治区",
                                                                      "新疆维吾尔自治区", "内蒙古自治区", "黑龙江省",
                                                                      "吉林省", "辽宁省", "河北省", "山西省", "山东省",
                                                                      "河南省", "江苏省", "安徽省", "浙江省", "福建省",
                                                                      "江西省", "湖南省", "湖北省", "广东省", "海南省",
                                                                      "北京市", "天津市", "上海市"]):
            data_dict[search_query] = data["result"][3]["data"]  # 只获取第四行数据
        elif quarters:
            quarter_data_dict = {}
            for i, quarter_data in enumerate(data["result"][:4][::-1]):
                quarter_data_dict[quarters[i]] = quarter_data["data"]
            data_dict[search_query] = quarter_data_dict
        else:
            data_dict[search_query] = data["result"][0]["data"]

        print(f"Fetched data for {year} - {search_query}: {data_dict[search_query]}")

    except (requests.RequestException, KeyError):
        print(f"Failed to fetch data for {year}")
    return data_dict


url = "https://data.stats.gov.cn/search.htm"
quarters = ["一", "二", "三", "四"]

queries = [
    "居民人均可支配收入基尼系数",
    "居民人均可支配收入_累计增长",
    "居民可支配收入中位数_累计增长",
    "居民人均可支配工资性收入_累计增长",
    "居民人均可支配经营净收入_累计增长",
    "居民人均可支配财产净收入_累计增长",
    "居民人均可支配转移净收入_累计增长"
]

all_data_by_year = {}
for year in range(2014, 2022):
    year_data = {}
    for query in queries:
        if "年" in query or "累计" in query:
            year_data.update(fetch_data(url, query, year, quarters))
        else:
            year_data.update(fetch_data(url, query, year))
    all_data_by_year[year] = year_data

print("Final data:")
print(all_data_by_year)



# 输出到 CSV 文件
with open('../Get_Chart/Data_csv/income_and_inequality_metrics_national.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    # 写入标题行
    header = ['年份_季度'] + queries
    csvwriter.writerow(header)

    # 遍历字典并写入数据
    for year, year_data in all_data_by_year.items():
        for quarter in quarters:
            row = [f"{year}_Q{quarter}"]

            for query in queries:
                quarter_data = year_data.get(query, {})
                if isinstance(quarter_data, dict):  # 假设数据是按季度存储的
                    row.append(quarter_data.get(quarter, 'N/A'))
                else:  # 如果数据不是按季度存储的
                    row.append(quarter_data if quarter_data else 'N/A')

            csvwriter.writerow(row)

print("CSV文件已创建")
