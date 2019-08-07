#!/bin/bash
# 安装pip以及相关模块
yum -y install epel-release
yum -y install python-pip python-devel.x86_64 gcc
pip install --upgrade pip
wget -P /tmp https://pypi.python.org/packages/source/p/psutil/psutil-2.1.3.tar.gz

cd /tmp
tar -zxvf psutil-2.1.3.tar.gz

cd psutil-2.1.3

python setup.py install
