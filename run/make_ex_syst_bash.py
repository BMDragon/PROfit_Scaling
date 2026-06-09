import sys

assert len(sys.argv) == 3, "Usage: python generateXML.py <Nbins> <tag>"

Nbins = sys.argv[1]
tag = sys.argv[2]

filename = 'ex_syst_' + str(Nbins) + 'bins'

file = open('./' + filename + '.sh', 'w')
file.write('''#!/bin/bash

MAX_JOBS=20
running=0
''')

for Npulls in range(0, 250, 5):
    systs = ''
    for i in range(0, Npulls, 1):
        systs += ' dummynorm' + str(i)

    file.write('''
(
    tag="''' + str(Nbins) + '''bins_''' + str(Npulls) + '''pulls"
    PROfit -x .././xml/scale_''' + str(Nbins) + '''bins_250pulls.xml --tag scaling_''' + str(Nbins) + '''bins_250pulls -v 1 -w 3 --log .././process_logs/log_${tag}.txt --progress --seed 314 --scale-by-width --exclude-systs''' + systs + ''' scale-test
    grep SCALE .././process_logs/log_${tag}.txt > .././scaling_outputs/scale_${tag}.txt
    echo "Finished $tag"
) &

((running++))
if (( running >= MAX_JOBS )); then
    wait -n    # wait for one job to finish
    ((running--))
fi
    ''')

file.write('''
wait
echo "All ''' + str(Nbins) + ''' jobs completed."
           ''')
