import requests
from config import constant
import fileUtils

# # 读取宿主机挂载的敏感信息
login_url = "./config/login/main.json"
userInfo = fileUtils.toJson(login_url)

# 请求配置
url = "https://langlangy.cn/login"
cookieKey = "sw110xy="

headers = constant.headers

payload = {
    "country_id": "",
    "mobile": "",
    "verify_code": "",  # 动态获取或替换
    "login_type": "PASS",
    "submit": "1"
}
for key in userInfo:
    payload[key] = userInfo[key]

def loginUser():
    # 执行请求
    session = requests.Session()
    session.headers.update(headers)
    # 先获取cookie
    getSetCookieVal = session.get(url, timeout=10).headers["Set-Cookie"]
    index = getSetCookieVal.find(cookieKey)
    tmp = getSetCookieVal[index:]  # sw110xy=3sc09rej3du9bd9m1320q50h3r5g9nj7; expires=...
    cookie = tmp[:tmp.find(";")]
    headers["cookie"] = cookie
    print("cookie: ", headers["cookie"])
    # 登录 重新创建已经会话
    session = requests.Session()
    session.headers.update(headers)
    response = session.post(url, data=payload, timeout=10)
    if response.text.find("2000") != -1:
        # 成功
        return cookie
    else:
        return ""


