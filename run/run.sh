#!/bin/bash

rerun_binaries=true

for Nbins in {100..1000..900}
do
    for Npulls in {10..1000..30}
    do
    (
        tag="${Nbins}bins_${Npulls}pulls"
        python generateXML.py $Nbins $Npulls $tag
        if $rerun_binaries; then
            (time PROfit -x .././xml/scale_${tag}.xml -t scaling${tag} process) > .././time_logs/log_${tag}_time.txt 2>&1
            grep user .././time_logs/log_${tag}_time.txt > .././time_logs/user_${tag}_time.txt
        fi
        PROfit -x .././xml/scale_${tag}.xml --tag scaling${tag} -v 1 -w 3 --log .././process_logs/log_${tag}.txt --progress --seed 314 --scale-by-width scale-test
        grep SCALE .././process_logs/log_${tag}.txt > .././scaling_outputs/scale_${tag}.txt
        echo "Finished ${Nbins} bins, ${Npulls} pulls"
    ) &
    done
done

for Mpulls in {40..640..600}
do
    for Mbins in {50..1500..50}
    do
    (
        tag="${Mbins}bins_${Mpulls}pulls"
        python generateXML.py $Mbins $Mpulls $tag
        if $rerun_binaries; then
            (time PROfit -x .././xml/scale_${tag}.xml -t scaling${tag} process) > .././time_logs/log_${tag}_time.txt 2>&1
            grep user .././time_logs/log_${tag}_time.txt > .././time_logs/user_${tag}_time.txt
        fi
        PROfit -x .././xml/scale_${tag}.xml --tag scaling${tag} -v 1 -w 3 --log .././process_logs/log_${tag}.txt --progress --seed 314 --scale-by-width scale-test
        grep SCALE .././process_logs/log_${tag}.txt > .././scaling_outputs/scale_${tag}.txt
        echo "Finished ${Mbins} bins, ${Mpulls} pulls"
    ) &
    done
done