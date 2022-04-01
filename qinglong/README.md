用于将容器内的JD_COOKIE上传到另一个容器内，用于向跑脚本的容器隐藏JD_WSCK

```
ql raw https://raw.githubusercontent.com/yuxian158/others_scripts/master/qinglong/index.py
```

config.sh填写示例

```
export ql_url="12.34.567.89"
export ql_post="5700"
export client_id="*********"
export client_secret="********"
export env_name="JD_COOKIE"
```

task_after.sh填写示例

```
#!/usr/bin/env bash
send_scripts="Zy143L_wskey_wskey" 
for str in $send_scripts
do
if [[ $log_path == *$str* ]];then
    task raw_qinglong_index.py
    echo "开始同步变量"
else
    echo "不包含"
fi
done
```