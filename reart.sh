#/bin/bash
#echo 'chu67925' | sudo -S service network-manager restart 
echo 'chu67925' | sudo -S ls
ps -aux | grep broadspi | awk '{print $2}' | sudo xargs kill -s KILL	
#sleep 330
echo 'chu67925' | sudo -S /usr/bin/python broadspi.py -i $1

