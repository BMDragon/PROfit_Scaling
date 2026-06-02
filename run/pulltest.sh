#!/bin/bash

nPulls=10
pulltype="spline"

tag="pulltest_${nPulls}${pulltype}"
python generateXML.py 100 $nPulls $tag
if [ ! -f "./scaling${tag}_prop.bin" ]; then
    (time PROfit -x .././xml/scale_${tag}.xml -t scaling${tag} process) > .././time_logs/log_${tag}_time.txt 2>&1
    grep user .././time_logs/log_${tag}_time.txt > .././time_logs/user_${tag}_time.txt
fi
PROfit -x .././xml/scale_${tag}.xml --tag scaling${tag} -v 1 -w 3 --log .././process_logs/log_${tag}.txt --progress --seed 314 --scale-by-width scale-test
grep SCALE .././process_logs/log_${tag}.txt > .././scaling_outputs/scale_${tag}.txt
echo "Finished pull test with $nPulls ${pulltype}s"