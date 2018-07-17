# coding:utf8
import requests
from bs4 import BeautifulSoup           # pip install beautifulsoup4
# from xlutils.copy import copy         # pip install xlutils

url_view_bugs = "http://192.168.90.248/mantis/view_all_bug_page.php"
# url_view_id = "http://192.168.90.248/mantis/view.php?id="       # 细节处理

# need your cookies
raw_cookies = "PHPSESSID=srb7illeam8u9qlged8mld; MANTIS_secure_session=1; MANTIS_STRING_COOKIE=tLmoABYiMvEhK3LA30JYF1MmRHtDGO-0SxmEZo5kvL8xe2VUTf-vEWaFwe7Au4yU; MANTIS_BUG_LIST_COOKIE=2043%2C2391%2C2387%2C2389%2C2071%2C2099%2C2117%2C2116%2C2118%2C2083%2C2082%2C2119%2C2121%2C2068%2C1983%2C2051%2C2059%2C1760; MANTIS_PROJECT_COOKIE=23; MANTIS_VIEW_ALL_COOKIE=283"

def getCookies(raw_cookies):
    newCookies = {}
    for line in raw_cookies.split(";"):
        key, value = line.split("=", 1)
        newCookies[key] = value
    return newCookies
def getText(data):
    texts = []
    for _data in data:
        texts.append(_data.text)
    return texts
def writeTxt():
    pass
# def writeExcel():
#     r_excel = open_workbook("问题单分析模板0601.xlsx")

class Mantis():
    def __init__(self):
        self.cookie = getCookies(raw_cookies)
        self.req_data = requests.post(url_view_bugs, cookies=self.cookie)
        self.soup = BeautifulSoup(self.req_data.text, "html.parser")
    def getID(self):
        "编号"
        all_id = self.soup.select("#buglist .column-id")
        return getText(all_id)
    def getSeverity(self):
        "严重性"
        all_severity = self.soup.select("#buglist .column-severity")
        return getText(all_severity)
    def getCategory(self):
        "分类"
        all_category = self.soup.select("#buglist .column-category")
        return getText(all_category)
    def getSummary(self):
        "摘要"
        all_summary = self.soup.select("#buglist .column-summary")
        return getText(all_summary)
    def getUrl(self, _id):
        return "http://192.168.90.248/mantis/view.php?id=%d" % int(_id)
    def getDetails(self, _id):
        _url = self.getUrl(_id)
        req_details = requests.post(_url, cookies=self.cookie)
        return req_details.text

    def get_details(self, _id):
        "details deal"
        details = {}
        _details = self.getDetails(_id)
        det = BeautifulSoup(_details, "html.parser")
        _details_reporter = det.select(".table-bordered.table-condensed .bug-reporter")[1]      # 报告者
        _details_priority = det.select(".table-bordered.table-condensed .bug-priority")[1]      # 优先级
        _details_happen = det.select(".table-bordered.table-condensed .bug-reproducibility")[1] # 出现频率
        details["id"] = _id
        details["reporter"] = _details_reporter.text
        details["priority"] = _details_priority.text
        details["happen"] = _details_happen.text
        return details
    def saveTotxt(self, data):
        files = open("f.html","a")
        files.write(str(data))
        files.close()
    def writeTotxt(self):
        f = open("f.txt","a")
        ids = self.getID()
        severitys = self.getSeverity()
        categorys = self.getCategory()
        summarys = self.getSummary()
        lens = len(ids)
        for i in range(1,lens):
            details = self.get_details(ids[i])
            newdatas = details["id"] + '\t' + details["reporter"] + '\t'  + details["priority"] + '\t' \
                   + severitys[i] + '\t'  + details["happen"] + '\t'  + categorys[i] + '\t' \
                   + summarys[i] + '\n'
            f.write(newdatas)
        f.close()
if __name__ == "__main__":
    m = Mantis()
    m.writeTotxt()
    print("end~")
