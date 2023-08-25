import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 爬取国家统计局数据
# 居民人均可支配收入(元)
def spider_disposable_income_of_residents():
    url = "https://data.stats.gov.cn/search.htm"
    rate_list = []  # 使用一个新列表来保存所有数据
    for year in (range(2014, 2022)):
        parameters = {
            "s": f"{year}可支配收入",  # f{year}代表格式化字符串
            "m": "searchdata",
            "db": "",
            "p": "0"
        }
        time.sleep(1)
        try:
            # 模拟发送请求
            response = requests.get(url, params=parameters, verify=False)
            response.raise_for_status()
            # 获取网页状态码
            data = response.json()
            rate_list.append((year, data["result"][0]["data"]))
            print(f"{year}年居民可支配收入：{data['result'][0]['data']}")

        except (requests.RequestException, KeyError):
            print(f"Failed to fetch data for {year}")


# 居民人均可支配收入累计值(元)(季度)
def spider_disposable_income_of_residents_cumulative_value():
    url = "https://data.stats.gov.cn/search.htm"
    rate_list = []  # 使用一个新列表来保存所有数据
    quarters = ["一", "二", "三", "四"]
    for year in range(2020, 2022):
        parameters = {
            "s": f"{year}年居民可支配收入累计值",  # 搜索整年的数据
            "m": "searchdata",
            "db": "",
            "p": "0"
        }
        time.sleep(1)  # 休眠1秒以防止被封
        try:
            # 模拟发送请求
            response = requests.get(url, params=parameters, verify=False)
            response.raise_for_status()
            # 获取网页状态码
            data = response.json()

            # 假设data["result"]是一个包含四个季度数据的列表
            for i, quarter_data in enumerate(data["result"][:4][::-1]):  # 逆序处理
                rate_list.append((year, quarters[i], quarter_data["data"]))
                print(f"{year}年第{quarters[i]}季度居民可支配收入累计值：{quarter_data['data']}")

        except (requests.RequestException, KeyError):
            print(f"Failed to fetch data for {year}")


# 居民人均可支配收入累计增长(季度)
def spider_disposable_income_of_residents_cumulative_growth():
    url = "https://data.stats.gov.cn/search.htm"
    rate_list = []  # 使用一个新列表来保存所有数据
    quarters = ["一", "二", "三", "四"]
    for year in range(2020, 2022):
        parameters = {
            "s": f"{year}年居民可支配收入累计增长",  # 搜索整年的数据
            "m": "searchdata",
            "db": "",
            "p": "0"
        }
        time.sleep(1)  # 休眠1秒以防止被封
        try:
            # 模拟发送请求
            response = requests.get(url, params=parameters, verify=False)
            response.raise_for_status()
            # 获取网页状态码
            data = response.json()

            # 假设data["result"]是一个包含四个季度数据的列表
            for i, quarter_data in enumerate(data["result"][:4][::-1]):  # 逆序处理
                rate_list.append((year, quarters[i], quarter_data["data"]))
                print(f"{year}年第{quarters[i]}季度居民人均可支配收入_累计增长(%)：{quarter_data['data']}")

        except (requests.RequestException, KeyError):
            print(f"Failed to fetch data for {year}")


# 居民人均可支配收入中位数(元)
def spider_Median_per_capita_disposable_income_of_residents():
    url = "https://data.stats.gov.cn/search.htm"
    rate_list = []  # 使用一个新列表来保存所有数据
    for year in (range(2020, 2022)):
        parameters = {
            "s": f"{year}居民可支配收入中位数",  # f{year}代表格式化字符串
            "m": "searchdata",
            "db": "",
            "p": "0"
        }
        time.sleep(1)
        try:
            # 模拟发送请求
            response = requests.get(url, params=parameters, verify=False)
            response.raise_for_status()
            # 获取网页状态码
            data = response.json()
            rate_list.append((year, data["result"][0]["data"]))
            print(f"{year}年居民可支配收入中位数：{data['result'][0]['data']}")
        except (requests.RequestException, KeyError):
            print(f"Failed to fetch data for {year}")


# 居民人均可支配收入中位数累计值(元)(季度)
def spider_Median_per_capita_disposable_income_of_residents_cumulative_value():
    url = "https://data.stats.gov.cn/search.htm"
    rate_list = []  # 使用一个新列表来保存所有数据
    quarters = ["一", "二", "三", "四"]
    for year in range(2020, 2022):
        parameters = {
            "s": f"{year}年居民可支配收入中位数累计值",  # 搜索整年的数据
            "m": "searchdata",
            "db": "",
            "p": "0"
        }
        time.sleep(1)  # 休眠1秒以防止被封
        try:
            # 模拟发送请求
            response = requests.get(url, params=parameters, verify=False)
            response.raise_for_status()
            # 获取网页状态码
            data = response.json()

            # 假设data["result"]是一个包含四个季度数据的列表
            for i, quarter_data in enumerate(data["result"][:4][::-1]):  # 逆序处理
                rate_list.append((year, quarters[i], quarter_data["data"]))
                print(f"{year}年第{quarters[i]}季度居民可支配收入中位数累计值：{quarter_data['data']}")

        except (requests.RequestException, KeyError):
            print(f"Failed to fetch data for {year}")


# 居民人均可支配收入中位数累计增长(季度)
def spider_Median_per_capita_disposable_income_of_residents_cumulative_growth():
    url = "https://data.stats.gov.cn/search.htm"
    rate_list = []  # 使用一个新列表来保存所有数据
    quarters = ["一", "二", "三", "四"]
    for year in range(2020, 2022):
        parameters = {
            "s": f"{year}年居民可支配收入中位数累计增长",  # 搜索整年的数据
            "m": "searchdata",
            "db": "",
            "p": "0"
        }
        time.sleep(1)  # 休眠1秒以防止被封
        try:
            # 模拟发送请求
            response = requests.get(url, params=parameters, verify=False)
            response.raise_for_status()
            # 获取网页状态码
            data = response.json()

            # 假设data["result"]是一个包含四个季度数据的列表
            for i, quarter_data in enumerate(data["result"][:4][::-1]):  # 逆序处理
                rate_list.append((year, quarters[i], quarter_data["data"]))
                print(f"{year}年第{quarters[i]}季度居民可支配收入中位数累计增长：{quarter_data['data']}")

        except (requests.RequestException, KeyError):
            print(f"Failed to fetch data for {year}")



# 居民人均可支配收入基尼系数
def spider_Gini_coefficient_of_per_capita_disposable_income_of_residents():
    url = "https://data.stats.gov.cn/search.htm"
    rate_list = []  # 使用一个新列表来保存所有数据
    for year in (range(2020, 2022)):
        parameters = {
            "s": f"{year}居民可支配收入基尼系数",  # f{year}代表格式化字符串
            "m": "searchdata",
            "db": "",
            "p": "0"
        }
        time.sleep(1)
        try:
            # 模拟发送请求
            response = requests.get(url, params=parameters, verify=False)
            response.raise_for_status()
            # 获取网页状态码
            data = response.json()
            rate_list.append((year, data["result"][0]["data"]))
            print(f"{year}年居民可支配收入基尼系数：{data['result'][0]['data']}")
        except (requests.RequestException, KeyError):
            print(f"Failed to fetch data for {year}")







if __name__ == '__main__':
    spider_disposable_income_of_residents()
    # spider_Median_per_capita_disposable_income_of_residents()
    # spider_Gini_coefficient_of_per_capita_disposable_income_of_residents()
    # spider_disposable_income_of_residents_cumulative_value()
    # spider_disposable_income_of_residents_cumulative_growth()
    # spider_Median_per_capita_disposable_income_of_residents_cumulative_value()
    # spider_Median_per_capita_disposable_income_of_residents_cumulative_growth()
