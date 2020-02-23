---

### 项目说明

---

### 此项目停止维护，将使用go重构，增加扩展性!!!
### 此项目停止维护，将使用go重构，增加扩展性!!!
### 此项目停止维护，将使用go重构，增加扩展性!!!

### 主要技术 flask + gunicorn + nginx 

- 作用： 一些自己做的api
- 作者： jeeysie@gmail.com
- 时间： 2019-01-18

### 服务模块

##### 1. root , 一些项目整体的配置

##### 2. apps , 一些应用模块

- webhook 提供一些平台的webhook服务转发
- link 提供网址压缩等一些关于网址的服务

### 开机自启说明

```
# 拷贝docs下的webhook.sh到 /etc/init.d/下
# 添加执行权限
chmod +x webhook.sh
# 注册服务
chkconfig --add webhook.sh
# 开机自启
chkconfig webhook.sh on
```
