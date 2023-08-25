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
    "全国居民人均可支配收入",
    "云南省 居民人均可支配收入",
    "贵州省 居民人均可支配收入",
    "四川省 居民人均可支配收入",
    "广西壮族自治区 居民人均可支配收入",
    "重庆市 居民人均可支配收入",
    "西藏自治区 居民人均可支配收入",
    "陕西省 居民人均可支配收入",
    "甘肃省 居民人均可支配收入",
    "青海省 居民人均可支配收入",
    "宁夏回族自治区 居民人均可支配收入",
    "新疆维吾尔自治区 居民人均可支配收入",
    "内蒙古自治区 居民人均可支配收入",
    "黑龙江省 居民人均可支配收入",
    "吉林省 居民人均可支配收入",
    "辽宁省 居民人均可支配收入",
    "河北省 居民人均可支配收入",
    "山西省 居民人均可支配收入",
    "山东省 居民人均可支配收入",
    "河南省 居民人均可支配收入",
    "江苏省 居民人均可支配收入",
    "安徽省 居民人均可支配收入",
    "浙江省 居民人均可支配收入",
    "福建省 居民人均可支配收入",
    "江西省 居民人均可支配收入",
    "湖南省 居民人均可支配收入",
    "湖北省 居民人均可支配收入",
    "广东省 居民人均可支配收入",
    "海南省 居民人均可支配收入",
    "北京市 居民人均可支配收入",
    "天津市 居民人均可支配收入",
    "上海市 居民人均可支配收入",
    "居民人均可支配收入基尼系数",
    "居民人均可支配收入_累计值",
    "居民人均可支配收入_累计增长",
    "居民可支配收入中位数",
    "居民可支配收入中位数_累计值",
    "居民可支配收入中位数_累计增长",
    "居民人均可支配工资性收入_累计值",
    "居民人均可支配工资性收入_累计增长",
    "居民人均可支配经营净收入_累计值",
    "居民人均可支配经营净收入_累计增长",
    "居民人均可支配财产净收入_累计值",
    "居民人均可支配财产净收入_累计增长",
    "居民人均可支配转移净收入_累计值",
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

with open('../Get_Chart/Data_csv/disposable_income_by_province.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    # 获取所有唯一的省份
    unique_provinces = set()
    for year_data in all_data_by_year.values():
        for query in year_data.keys():
            if "居民人均可支配收入" in query and "全国" not in query:
                unique_provinces.add(query.replace(" 居民人均可支配收入", ""))

    # 写入标题行
    header = ['年份', '全国'] + list(sorted(unique_provinces))  # 例如：['年份', '全国', '北京', '上海', ...]
    csvwriter.writerow(header)

    # 遍历字典并写入数据
    for year, year_data in all_data_by_year.items():
        row = [year]

        # 添加全国数据
        national_data = year_data.get("全国居民人均可支配收入", 'N/A')
        row.append(national_data)

        # 添加各省份数据
        for province in sorted(unique_provinces):
            province_key = f"{province} 居民人均可支配收入"
            row.append(year_data.get(province_key, 'N/A'))  # 如果没有数据，写入'N/A'

        csvwriter.writerow(row)

print("CSV文件已创建")

