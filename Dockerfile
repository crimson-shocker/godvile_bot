# This Dockerfile is used to build an sakuli image based on Ubuntu

FROM consol/ubuntu-xfce-vnc

RUN apt-get update && \apt-get install -y python3-pip

EXPOSE 5901
RUN locale-gen ru_RU.UTF-8 
ADD godville.py /opt/godville.py
ADD locale /etc/default/locale
RUN pip3 install selenium  &&  chmod +x /opt/godville.py
