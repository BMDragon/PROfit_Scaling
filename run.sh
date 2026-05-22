#!/bin/bash

for i in {10..20..10}
do
(
    python generateXML.py $i 10
    time (PROfit -x ./xml/scale_${i}bins_10pulls.xml -t scaling${i}bins_10pulls process) > ./time_logs/log_${i}bins_10pulls_time.txt
    PROfit -x ./xml/scale_${i}bins_10pulls.xml --tag scaling${i}bins_10pulls -v 1 -w 3 --log ./process_logs/log_${i}bins_10pulls.txt --progress --seed 314 --scale-by-width scale-test
    grep SCALE ./process_logs/log_${i}bins_10pulls.txt > scale_${i}bins_10pulls.txt
    echo "Finished ${i} bins, 10 pulls"
) &
done