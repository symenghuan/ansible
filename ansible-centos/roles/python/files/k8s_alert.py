#!/usr/bin/env python
# -*- coding:utf-8 -*-

import paramiko
import os
import signal
import datetime

# 设置主机列表
host_list = ({'ip': '10.82.12.93', 'port': 22, 'username': 'root', 'password': '123abcABC'},)

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# 远程连接主机获取内存使用率
def connssh(hostname, port, username, password):
    def handler(signum, frame):
        raise AssertionError
    str_out = None
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(3)
        conn.connect(hostname, port, username, password)
        signal.alarm(0)
        stdin, stdout, stderr = conn.exec_command('python /home/get_mem.py')
        str_out = stdout.read().decode()
        return str_out
        conn.close()
    except Exception as e:
        return str_out


if __name__ == "__main__":
    for host in host_list:
        try:
            result = connssh(hostname=host['ip'], port=host['port'], username=host['username'], password=host['password'])
            msg = os.popen("kubectl get nodes|grep %s|awk '{print $2}'" % host['ip'])
            node = msg.read().strip('\n')
            if result is not None and float(result) > 85:
                if node == "Ready":
                    exc = os.system("kubectl cordon %s" % host['ip'])
                    if exc == 0:
                        print("%s Node %s is cordoned, The current memory %s%%" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),host['ip'],result.strip('\n')))
                    else:
                        print("%s Node %s is not cordoned, The current memory %s%%" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),host['ip'],result.strip('\n')))
                else:
                    print("%s Node %s is not Ready, The current memory %s%%" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),host['ip'],result.strip('\n')))
            elif result is not None and float(result) <= 85:
                if node != "Ready":
                    exc = os.system("kubectl uncordon %s" % host['ip'])
                    if exc == 0:
                        print("%s Node %s is uncordoned, The current memory %s%%" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),host['ip'],result.strip('\n')))
                    else:
                        print("%s Node %s is not uncordoned, The current memory %s%%" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),host['ip'],result.strip('\n')))
                else:
                    print("%s Node %s is Readyr, The current memory %s%%" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),host['ip'], result.strip('\n')))
            else:
                print(result.strip('\n'))
            msg.close()
        except Exception as e:
            print("%s %s connect timeout!" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),host['ip']))

