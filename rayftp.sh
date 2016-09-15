#!/bin/sh
#cd ShanghaiB
ftp -n 192.168.11.12 << EOF
user ray G6UoXc2j
bin
cd Scan
get Winter_final2_prv1.mid
quit
EOF
sudo chmod -R 775 .

