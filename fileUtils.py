import json


def toJson(fileUrl):
    # 打开 JSON 文件并加载为 Python 对象
    with open(fileUrl, 'r', encoding='utf-8') as f:
        data = json.load(f)  # 将文件内容转换为字典或列表
        return data
