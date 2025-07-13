from time import sleep
from datetime import datetime

import emailUtils
import login
import renew
import requests
import fileUtils

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
isSuccessful = 0
emailData = None
constants = None
cookie = ""
err = None

print(f"--------------------  START {datetime.now().strftime(TIME_FORMAT)}  ----------------------")
try:
    main_dir = "./config/main/"
    email_url = "./config/email/main.json"

    constants = fileUtils.toJson(main_dir + "constant.json")
    emailData = fileUtils.toJson(email_url)



    # 登录并获取cookie

    for i in range(constants["maxLoginTimes"]):
        try:
            cookie = login.loginUser()
            break
        except requests.exceptions.RequestException as e:
            err = e
            print(f"请求失败: {e}")
            sleep(5)
    if err is not None or cookie == "":
        err = f"用户名或密码错误"
        exit(10)
    # 循环更新
    serviceIdList = constants["serviceIdList"]
    errServiceIdList = []
    for serviceId in serviceIdList:
        if renew.renewService(cookie, serviceId) == -1:
            errServiceIdList.append(serviceId)
    # 判断是否成功
    if len(errServiceIdList) != 0:
        err = f"有服务延迟失败 {errServiceIdList}"
    else:
        isSuccessful = 1
except Exception as e:
     err = e
finally:
    if isSuccessful == 1:
        emailUtils.send(emailData["sender_email"],
                        emailData["sender_email"],
                        "浪浪云自动更新",
                        "自动更新成功 cookie: " + cookie)
    else:
        emailUtils.send(emailData["sender_email"],
                        emailData["sender_email"],
                        "浪浪云自动更新",
                        f"自动更新失败 err: {err}")

    print(f"-------------------  END TIME: {datetime.now().strftime(TIME_FORMAT)} -----------------------")
