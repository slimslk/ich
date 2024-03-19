USER=Dmytro
date
echo "hello $USER"
pwd
ps -ef | grep -v grep | grep bioset | wc -l
ls -la /etc/passwd | awk {'print $1'}
