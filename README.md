---

### 项目说明

---

### 主要技术 flask + gunicorn + nginx 

- 作用： 提供dev.tencent.com（原coding）的webhook转发服务
- 作者： cn.lujianxin@gmail.com
- 时间： 2019-01-18

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
