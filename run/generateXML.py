# Created by Brandon Weiss on 5/22/2026

import sys

assert len(sys.argv) == 4, "Usage: python generateXML.py <Nbins> <Npulls> <tag>"

Nbins = sys.argv[1]
Npulls = sys.argv[2]
tag = sys.argv[3]

list_of_norms = ["FiducialVol", "FluxNorm", "ICARUSDet", "SBNDDet", "Targets_POT"]

list_of_splines = []
with open('./listOfSplines.txt', 'r') as f:
    for line in f:
        list_of_splines.append(line.strip())

filename = 'scale_' + str(tag)

file = open('.././xml/' + filename + '.xml', 'w')
file.write('''
<?xml version="1.0" ?>

<!-- One Mode -->
<mode name="nu" />

<!-- One Detector SBN Analysis-->
<detector name="SBND" pot="9.7e20"/>

<!-- Two Channels, numu and nue selections -->
<channel name="numu" plotname="#nu_{#mu} Selection">
    <bins unit = "Reconstructed Neutrino Energy [GeV]" min="0.2" max="3" nbins="''' + str(Nbins) + '''" />
    <bins unit = "True Neutrino Energy [GeV]" min="0" max="3" nbins="''' + str(Nbins) + '''"/>
    <bins unit = "True L/E" min="0" max="3" nbins="''' + str(Nbins) + '''" plot="false"/>
    <subchannel name="numucc" plotname="#nu_{#mu} CC" color="#99CCFF"/>
</channel>

<!-- The Physics model, here nue-appearance only -->
<model tag="nueapp">
    <rule index="0" name="No Osc"/>
    <rule index="1" name="Nue App"/>
    <parameter variable_index = "2" name="L/E"/>
</model>

<!-- Where to find the Montecarlo and how to fill all the subchannels defined above-->
<MCFile treename="events/selectedNu" filename="/nevis/riverside/data/leehagaman/PROfit_files/Tutorial2025/sbnd_bnbcv_files_localtest.txt" scale = "1.0" pot="2.15692e19">
    <friend treename="events/multisigmaTree" />
    <friend treename="events/multisimTree" />
    <branch
        associated_subchannel = "nu_SBND_numu_numucc"
        model_rule            = "0"
        additional_weight     = "0.9*CC*(truePDG == 14 || truePDG == -14)*(recoE>0)"
        >
        <variable>recoE</variable>
        <variable>trueE</variable>
        <variable>trueL/(trueE*1000.0)</variable>
    </branch>
</MCFile>


<systematics>
    <!-- Inlcude MC stats, uncomment out to remove -->
    <systematic type="mcstat" plotname="MC Stats" tag="Other">MCStat</systematic>

''')

for i in range(int(Npulls)):
    if i < len(list_of_norms):
        norm = list_of_norms[i]
        file.write('    <systematic type="norm" plotname="' + norm + '" tag="Other">' + norm + ':0.02</systematic>\n')
    else:
        file.write('    <systematic type="norm" plotname="dummynorm' + str(i) + '" tag="Other">dummynorm' + str(i) + ':0.02</systematic>\n')
'''
for i in range(int(Npulls)):
    spline = list_of_splines[i % len(list_of_splines)]
    file.write('    <systematic type="spline"  binning="var0" plotname="' + spline + '" tag="Other">' + spline + '</systematic>\n')
    #file.write('    <systematic type="spline"  binning="var0" plotname="ZExpA1CCQE" tag="Zexpansion">GENIEReWeight_SBN_v1_multisigma_ZExpA1CCQE</systematic>\n')
'''

file.write('''

    <systematic type="covariance" plotname="NCELVariationResponse" tag="Cross-Section-I">GENIEReWeight_SBN_v1_multisim_NCELVariationResponse</systematic>
    <systematic type="covariance" plotname="NCRESVariationResponse" tag="Cross-Section-I">GENIEReWeight_SBN_v1_multisim_NCRESVariationResponse</systematic>
    <systematic type="covariance" plotname="COHVariationResponse" tag="Cross-Section-I">GENIEReWeight_SBN_v1_multisim_COHVariationResponse</systematic>
    <systematic type="covariance" plotname="DISBYVariationResponse" tag="Cross-Section-I">GENIEReWeight_SBN_v1_multisim_DISBYVariationResponse</systematic>
    <systematic type="covariance" plotname="FSI_pi" tag="Cross-Section-II-FSI">GENIEReWeight_SBN_v1_multisim_FSI_pi_VariationResponse</systematic>
    <systematic type="covariance" plotname="FSI_N" tag="Cross-Section-II-FSI">GENIEReWeight_SBN_v1_multisim_FSI_N_VariationResponse</systematic>
    <systematic type="covariance" plotname="NormNCMEC" tag="Cross-Section-I">GENIEReWeight_SBN_v1_multisim_NormNCMEC</systematic>
    <systematic type="covariance" plotname="NonRESBGvpCC1pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvpCC1pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvpCC2pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvpCC2pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvpNC1pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvpNC1pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvpNC2pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvpNC2pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvnCC1pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvnCC1pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvnCC2pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvnCC2pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvnNC1pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvnNC1pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvnNC2pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvnNC2pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvbarpCC1pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvbarpCC1pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvbarpCC2pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvbarpCC2pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvbarpNC1pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvbarpNC1pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvbarpNC2pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvbarpNC2pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvbarnCC1pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvbarnCC1pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvbarnCC2pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvbarnCC2pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvbarnNC1pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvbarnNC1pi</systematic>
    <systematic type="covariance" plotname="NonRESBGvbarnNC2pi" tag="Cross-Section-III-NonRes">GENIEReWeight_SBN_v1_multisim_NonRESBGvbarnNC2pi</systematic>
    
    <!-- use all flux covariance systs from multisimTree-->
    <systematic type="covariance" tag="Flux">expskin_Flux</systematic>
    <systematic type="covariance" tag="Flux">horncurrent_Flux</systematic>
    <systematic type="covariance" tag="Flux">nucleoninexsec_Flux</systematic>
    <systematic type="covariance" tag="Flux">nucleonqexsec_Flux</systematic>
    <systematic type="covariance" tag="Flux">nucleontotxsec_Flux</systematic>
    <systematic type="covariance" tag="Flux">pioninexsec_Flux</systematic>
    <systematic type="covariance" tag="Flux">pionqexsec_Flux</systematic>
    <systematic type="covariance" tag="Flux">piontotxsec_Flux</systematic>
    <systematic type="covariance" tag="Flux">piplus_Flux</systematic>
    <systematic type="covariance" tag="Flux">piminus_Flux</systematic>
    <systematic type="covariance" tag="Flux">kplus_Flux</systematic>
    <systematic type="covariance" tag="Flux">kminus_Flux</systematic>
    <systematic type="covariance" tag="Flux">kzero_Flux</systematic>
</systematics>

''')

print('Finished making ' + filename +'.xml')