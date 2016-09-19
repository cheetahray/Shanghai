#/bin/bash
#echo '20233153jq' | sudo -S service network-manager restart 
echo '20233153jq' | sudo -S ls
ps -aux | grep broadspi | awk '{print $2}' | sudo xargs kill -s KILL	
#sleep 330
echo '20233153jq' | sudo -S /usr/bin/python broadspi.py -i $1

