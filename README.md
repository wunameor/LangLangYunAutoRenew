# 本项目是关于浪浪云延迟脚本命令 是基于docker运行的
## 镜像构建运行
1. 在当前目录的上级复制 devp 里面的相关内容
2. 在当前目录创建 app 这个目录
3. 进入这个目录 把除了 devp、.gitignore、README.md 的文件拷贝到app这个目录下
4. 回到上一级目录
5. 执行 docker compose build 
6. 然后执行 docker compose up -d
## 环境配置
1. 配置内容都在config 内
2. 邮件配置 email 
   1. "smtp_port": 465,
   2. "smtp_server": "smtp.qq.com",
   3. "sender_email": "your_email",
   4. "sender_password": "your_password"
3. 登录配置 login: 
   1. "username": "your_account", # 账户名
   2. "password": "your_password" # 密码
4. 主函数配置 main: 
   1. "maxLoginTimes": 3, # 最大登录次数
   2. "serviceIdList": [5551] # 服务订单Id列表
5. 定时任务配置 crontab
6. 环境依赖配置 requirements.txt
