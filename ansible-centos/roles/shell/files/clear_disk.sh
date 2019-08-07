#!/bin/bash
disk=`df -hP|grep root|awk '{print $5}'|awk -F"%" '{print $1}'`

cd /var/lib/docker/containers
dockerusg=`find . -type f -exec du -k {} \;| sort -nrk 1|head -n 4|awk '{print $2}'`
if [ $disk -ge 95 ]; then
      echo "$dockerusg" | while read line
          do
	      cat /dev/null > $line
	  done
fi
