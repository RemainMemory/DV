import requests
import time
import pymysql
import urllib3

urllib3.disable_warnings()


# 爬取国家统计局网站
def splider(request):
    url = "https://data.stats.gov.cn/search.htm"
    # 创建一个空列表
    list = []
    for year in (range(2010, 2023)):
        # 请求参数
        params = {
            "s": str(year) + "人口出生率",
            "m": "searchdata",
            "db": "",
            "p": 0
        }
        # 睡眠，每隔3秒请求一次
        time.sleep(3)
        # verify=False 关闭证书验证
        rs = requests.get(url, params=params, verify=False)
        # 获取json数据
        data = rs.json()
        print("%s年的出生率%s" % (year, data["result"][0]["data"]))
        # 定义一个元祖
        t = (year, data["result"][0]["data"])
        # 把元祖添加到空列表中
        list.append(t)
    print(list)
    addStudent(list)
    return "爬取成功"


# 新增函数 list =[(2010,11.9),(2011,12.9)]]
def addStudent(list):
    # 第一步：创建数据库连接
    con = pymysql.connect(
        host="localhost",  # 主机地址
        port=3306,  # 端口号
        user="root",  # 用户名
        passwd="CFY.20010214",  # 密码
        db="kmlg",  # 数据库名
        charset="utf8"  # 中文字符集
    )
    # 第二步:获取游标对象(运行sql语句的对象)
    cur = con.cursor()
    # 第三步:定义sql语句
    sql = "insert into people (`year`,rate) values(%s,%s);"
    # 第四步：运行sql
    cur.executemany(sql, list)
    # 第五步：提交事务
    con.commit()
    # 第六步：获取运行sql是否成功的返回值
    num = cur.rowcount
    if num > 0:
        print("新增成功")
        return "爬取成功"
    else:
        print("新增失败")
        return "爬取失败"

    # 第七步:关闭资源
    cur.close()
    con.close()


if __name__ == "__main__":
    splider()
