# 使用轻量级 Python 镜像
FROM python:3.11-slim

# 替换 Debian 官方源和安全更新源为阿里云镜像
RUN sed -i 's#http://deb.debian.org/debian#http://mirrors.aliyun.com/debian#g' /etc/apt/sources.list.d/debian.sources && \
    sed -i 's#http://security.debian.org/debian-security#http://mirrors.aliyun.com/debian-security#g' /etc/apt/sources.list.d/debian.sources

# 安装 cron 和基础依赖
RUN apt-get update && apt-get install -y cron \
    && rm -rf /var/lib/apt/lists/*

# 创建工作目录
WORKDIR /app

# 复制代码和依赖文件
COPY ./app/config/requirements.txt ./config/requirements.txt

# 安装依赖
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple  && \
    pip install --upgrade pip && \
    pip install -r ./config/requirements.txt

COPY ./app .
# 配置定时任务
COPY ./app/config/crontab /etc/cron.d/my-cron
RUN chmod 0644 /etc/cron.d/my-cron && \
    crontab /etc/cron.d/my-cron

# 启动 cron 并保持容器运行
CMD ["cron", "-f"]