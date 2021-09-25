#!/bin/bash

#將ASF的輸出傳到line


a=(docker ps -aq --no-trunc -f "name=asf")  #取得container id
count=$(wc /var/lib/docker/containers/$a/$a-json.log | awk '{print  $1}')  #計算原本檔案行數

#當行數不同，也代表檔案有變動時，取出第 (count+1)行後傳送到Line Notify，直到最新行
while [ true ]
do
  if [ "$(wc /var/lib/docker/containers/$a/$a-json.log | awk '{print $1}')" != "$count" ]; then   
    count=$(($count+1))
    message=$(tail -n +$count /var/lib/docker/containers/$a/$a-json.log| head -n 1 | jq -r '.log'| sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g")
    #echo $message
    curl -s -X POST -H 'Authorization: Bearer *******************************************' -F "message=$message" https://notify-api.line.me/api/notify > /dev/null
  fi
  sleep 1
done
