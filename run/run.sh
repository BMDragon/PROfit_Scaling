#!/bin/bash

for i in {50..500..25}
do
(
    python generateXML.py $i 10
    if [ ! -f "./scaling${i}bins_10pulls process" ]; then
        (time PROfit -x .././xml/scale_${i}bins_10pulls.xml -t scaling${i}bins_10pulls process) > .././time_logs/log_${i}bins_10pulls_time.txt 2>&1
        grep user .././time_logs/log_${i}bins_10pulls_time.txt > .././time_logs/user_${i}bins_10pulls_time.txt
    fi
    PROfit -x .././xml/scale_${i}bins_10pulls.xml --tag scaling${i}bins_10pulls -v 1 -w 3 --log .././process_logs/log_${i}bins_10pulls.txt --progress --seed 314 --scale-by-width scale-test
    grep SCALE .././process_logs/log_${i}bins_10pulls.txt > .././scaling_outputs/scale_${i}bins_10pulls.txt
    echo "Finished ${i} bins, 10 pulls"
) &
done