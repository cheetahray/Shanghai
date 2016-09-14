#!/bin/sh
#cd ShanghaiB
ftp -n 192.168.11.12 << EOF
user ray G6UoXc2j
bin
cd Scan
get Summer_midi_3.mid
quit
EOF
sudo chmod -R 775 .

