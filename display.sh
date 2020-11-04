#! /bin/sh
{
git pull
} 1>/dev/null 2>&1

#python3 display_milestones.py

#rm -rf png
#mkdir png
python3 convert.py
#python3 test.py


sleep 86400

./display.sh
