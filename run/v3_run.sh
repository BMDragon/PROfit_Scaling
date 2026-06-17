#!/bin/bash

MAX_JOBS=20
running=0

rerun_binaries=false

binvals=(1176 1314 1468 1641 1833 2048)

for Mbins in "${binvals[@]}"; do
(
    tag="${Mbins}bins_250pulls"
    python generateXML.py $Mbins 250 $tag
    if $rerun_binaries; then
        (time PROfit -x .././xml/scale_${tag}.xml -t scaling_${tag} process) > .././time_logs/log_${tag}_time.txt 2>&1
        grep user .././time_logs/log_${tag}_time.txt > .././time_logs/user_${tag}_time.txt
    fi
    PROfit -x .././xml/scale_${tag}.xml --tag scaling_${tag} -v 1 -w 3 --log .././process_logs/log_${tag}_v3.txt --progress --seed 314 --scale-by-width scale-test -N 500  --tests fillspectra,metric,metricgrad
    grep SCALE .././process_logs/log_${tag}_v3.txt > .././scaling_outputs/scale_${tag}_v3.txt
    echo "Finished ${Mbins} bins, 250 pulls"
) &

((running++))
if (( running >= MAX_JOBS )); then
    wait -n    # wait for one job to finish
    ((running--))
fi
done

wait

for Nbins in "${binvals[@]}"; do
    python make_ex_syst_bash_v3.py $Nbins
    bash ex_syst_${Nbins}bins_v3.sh
done
echo "All jobs completed."