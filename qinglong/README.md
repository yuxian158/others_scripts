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

