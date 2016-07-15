#!/usr/bin/env bash
set_ip=`cat ./passwd|grep ip|awk '{print $2}'`
case $1 in

  "-install")
    /usr/bin/docker build -f Dockerfile -t bot .
  ;;
  
  "-update")
    docker images |grep bot |awk '{print $3}' |xargs docker rmi
    cd /opt/godvile_bot/ && docker build -f Dockerfile -t bot .
  ;;

  "-h")
    echo 'Parm:'
    echo '-install'
    echo '-update:'
    echo '-h'
  ;;
  
    "-remove")
    docker images |grep bot |awk '{print $3}' |xargs docker rmi
    docker images |grep ubuntu-xfce-vnc |awk '{print $3}' |xargs docker rmi
  ;;

  
  *)
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++++ >>/var/log/bot.log
    echo `date +%F_%H:%M:%S` Start Bot  >>/var/log/bot.log
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++++ >>/var/log/bot.log
    /usr/bin/docker run  --rm  -p 10.0.5.100:5901:5901  --name godvile -v /opt/godvile_bot/:/opt/ bot /opt/godville.py >>/var/log/bot.log
    #/usr/bin/docker run  --rm  -p $set_ip:5901:5901  --name godvile -v /opt/godvile_bot/:/opt/ bot /opt/godville.py >>/var/log/bot.log
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++++ >>/var/log/bot.log
    echo `date +%F_%H:%M:%S` Stop Bot  >>/var/log/bot.log
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++++ >>/var/log/bot.log
  ;;
esac
