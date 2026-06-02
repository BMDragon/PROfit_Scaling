import uproot

files = [
    "/nevis/riverside/data/leehagaman/PROfit_files/Tutorial2025/sbnd_bnbcv_sBrucetree_197.root",
    "/nevis/riverside/data/leehagaman/PROfit_files/Tutorial2025/sbnd_bnbcv_sBrucetree_30.root",
    "/nevis/riverside/data/leehagaman/PROfit_files/Tutorial2025/sbnd_bnbcv_sBrucetree_31.root",
    "/nevis/riverside/data/leehagaman/PROfit_files/Tutorial2025/sbnd_bnbcv_sBrucetree_47.root",
    "/nevis/riverside/data/leehagaman/PROfit_files/Tutorial2025/sbnd_bnbcv_sBrucetree_89.root"
]

splines = set()

for i in range(len(files)):
    with uproot.open(files[i]) as f:
        keys = f["events/multisigmaTree"].keys()
        for key in keys:
            if key in ['Run', 'Subrun', 'Evt'] or "_sigma" in key:
                continue
            splines.add(key)
    f.close()

splines = sorted(splines)
file = open('./listOfSplines.txt', 'w')
for spline in splines:
    file.write(spline + '\n')
file.close()
