import requests
import csv
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetch_data(url, search_query, year, quarters=None):
    data_dict = {}
    parameters = {
        "s": f"{year}{search_query}",
        "m": "searchdata",
        "db": "",
        "p": "0"
    }
    try:
        response = requests.get(url, params=parameters, verify=False)
        response.raise_for_status()
        data = response.json()

        if quarters:
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


url = "https://data.stats.gov.cn/search.htm"  # 模拟的数据源
quarters = ["一", "二", "三", "四"]

queries = [
    "居民人均可支配收入_累计值",
    "居民人均可支配工资性收入_累计值",
    "居民人均可支配经营净收入_累计值",
    "居民人均可支配财产净收入_累计值",
    "居民人均可支配转移净收入_累计值"
]

all_data_by_year = {}
for year in range(2014, 2022):
    year_data = {}
    for query in queries:
        year_data.update(fetch_data(url, query, year, quarters))
    all_data_by_year[year] = year_data

# 输出到 CSV 文件
with open('../Get_Chart/Data_csv/disposable_income_national.csv', 'w', newline='', encoding='utf-8') as csvfile:
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
                row.append(quarter_data.get(quarter, 'N/A'))

            csvwriter.writerow(row)

print("CSV文件已创建")
