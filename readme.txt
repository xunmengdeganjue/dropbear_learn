dropbear Debug:
/usr/sbin/dropbear -v -E -F -P /var/run/dropbear.1.pid -p 22 -K 300 -T 3
-v 结合DEBUG_TRACE 可以将调试信息显示出来.

2020-09-29：
解决使用python脚本登录ssh执行命令时session未识别出来导致可以创建多session的问题。

