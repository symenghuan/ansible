# 找到docker-runc的位置，一般情况下在： /usr/bin/docker-runc
which docker-runc

# 备份原有的runc
mv /usr/bin/docker-runc /usr/bin/docker-runc.orig.$(date -Iseconds)

# 下载修复的runc
#curl -o /usr/bin/docker-runc -sSL https://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/runc/docker-runc-17.06-amd64
wget -O /usr/bin/docker-runc https://github.com/rancher/runc-cve/releases/download/CVE-2019-5736-build3/runc-v17.03.2-amd64

# 设置它的可执行权限
chmod +x /usr/bin/docker-runc

# 测试runc可以正常工作
docker-runc -v
# runc version 1.0.0-rc3
# commit: fc48a25bde6fb041aae0977111ad8141ff396438
# spec: 1.0.0-rc5
#docker run -it --rm ubuntu echo OK
