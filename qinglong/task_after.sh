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