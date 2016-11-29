#/bin/bash
echo '20233153jq' | sudo -S ls
ps -aux | grep broadspi | awk '{print $2}' | sudo xargs kill -s KILL

