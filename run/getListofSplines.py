files = [
    '/nevis/houston/home/bmw2176/Elephant_Vanishes/xml/PROfit_Tutorial_Oct2025v1_FullSBN_nue_app.xml',
    '/nevis/houston/home/bmw2176/Elephant_Vanishes/xml/PROfit_Tutorial_Oct2025v1_SPINE_ICARUS_numu_dis.xml',
    '/nevis/houston/home/bmw2176/Elephant_Vanishes/xml/uboone_with_splines/uboone_numuCCFCQ2_opendata_MA.xml',
    '/nevis/houston/home/bmw2176/Elephant_Vanishes/xml/uboone_with_splines/uboone_numuCCFCQ2_opendata_zexp_detvar.xml',
    '/nevis/houston/home/bmw2176/Elephant_Vanishes/xml/uboone_with_splines/uboone_spline_tutorial_numuCCNp0p_opendata_fast_nevis.xml',
    '/nevis/houston/home/bmw2176/Elephant_Vanishes/xml/uboone_with_splines/uboone_spline_tutorial_numuCCNp0p_opendata_fast.xml',
    '/nevis/houston/home/bmw2176/Elephant_Vanishes/xml/uboone_with_splines/uboone_spline_tutorial_numuCCNp0p_opendata_nevis.xml',
    '/nevis/houston/home/bmw2176/Elephant_Vanishes/xml/uboone_with_splines/uboone_spline_tutorial_numuCCNp0p_opendata.xml'
]

norms = set()
splines = set()

for i in range(len(files)):
    with open(files[i], 'r') as f:
        for line in f:
            if 'systematic type="norm"' in line:
                line_list = line.split(' ')
                for tag in line_list:
                    if 'plotname=' in tag:
                        norm = tag.split('=')[1].strip('"')
                        norms.add(norm)
            elif 'systematic type="spline"' in line:
                line_list = line.split(' ')
                for tag in line_list:
                    if 'plotname=' in tag:
                        spline = tag.split('=')[1].strip('"')
                        splines.add(spline)
            elif 'systematic type="spline_to_covariance"' in line:
                line_list = line.split(' ')
                for tag in line_list:
                    if 'plotname=' in tag:
                        spline = tag.split('=')[1].strip('"')
                        splines.add(spline)
    f.close()

norms = sorted(norms)
splines = sorted(splines)

file = open('./listOfSplines.txt', 'w')

file.write("type=\"norm\"\n")
for nm in norms:
    file.write(nm + '\n')
file.write("\n")

file.write("type=\"spline\"\n")
for spline in splines:
    file.write(spline + '\n')
file.close()
