# 延长服务器时间
import requests
from config import constant

# 请求配置
urlPattern="https://langlangy.cn/server/detail/${serviceId}/renew"
headers = constant.headers

data = {
    "month": 1,
    "coupon_id": 0,
    "no_use_activity": 0,
    "submit": 1,
}

session = requests.Session()
session.headers.update(headers)
def renewService(cookie, serviceId):
    if cookie == "": return -1
    try:
        headers["cookie"] = cookie
        url = urlPattern.replace("${serviceId}", str(serviceId))
        print("renew url: ", url)
        response = session.post(url, headers=headers, data=data, timeout=10)
        print(response.json())
        return serviceId
    except Exception as e:
        print(f"renew error: {e} serviceId {serviceId}")
        return -1
