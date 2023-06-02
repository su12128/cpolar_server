import requests
# url = "https://qpsearch.jd.com/relationalSearch?keyword=13900kf&ver=auto&client=pc&callback"  #搜索联想列表
url="https://search.jd.com/Search?keyword=13900kf&enc=utf-8&pvid=7485b0a3ee144ccf9fda9b51d867031c"

res = requests.get(url=url).text
with open("./search.html",'a',encoding="utf-8") as f:
    f.write(res)
print(res)