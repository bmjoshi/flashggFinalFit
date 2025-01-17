# USAGE: python tools/checkYields.py 2023-03-02
import sys
from os import access,F_OK

ext = sys.argv[1]

fits = ["xsec","ALT_0M","ALT_0PH","ALT_L1","ALT_L1Zg"]

allcats = ["RECO_0J_PTH_0_10_Tag0","RECO_0J_PTH_0_10_Tag1","RECO_0J_PTH_0_10_Tag2","RECO_0J_PTH_GT10_Tag0","RECO_0J_PTH_GT10_Tag1","RECO_0J_PTH_GT10_Tag2","RECO_1J_PTH_0_60_Tag0","RECO_1J_PTH_0_60_Tag1","RECO_1J_PTH_0_60_Tag2","RECO_1J_PTH_120_200_Tag0","RECO_1J_PTH_120_200_Tag1","RECO_1J_PTH_120_200_Tag2","RECO_1J_PTH_60_120_Tag0","RECO_1J_PTH_60_120_Tag1","RECO_1J_PTH_60_120_Tag2","RECO_GE2J_PTH_0_60_Tag0","RECO_GE2J_PTH_0_60_Tag1","RECO_GE2J_PTH_0_60_Tag2","RECO_GE2J_PTH_120_200_Tag0","RECO_GE2J_PTH_120_200_Tag1","RECO_GE2J_PTH_120_200_Tag2","RECO_GE2J_PTH_60_120_Tag0","RECO_GE2J_PTH_60_120_Tag1","RECO_GE2J_PTH_60_120_Tag2","RECO_PTH_200_300_Tag0","RECO_PTH_200_300_Tag1","RECO_PTH_300_450_Tag0","RECO_PTH_300_450_Tag1","RECO_PTH_450_650_Tag0","RECO_PTH_GT650_Tag0","RECO_THQ_LEP","RECO_TTH_HAD_PTH_0_60_Tag0","RECO_TTH_HAD_PTH_0_60_Tag1","RECO_TTH_HAD_PTH_0_60_Tag2","RECO_TTH_HAD_PTH_120_200_Tag0","RECO_TTH_HAD_PTH_120_200_Tag1","RECO_TTH_HAD_PTH_120_200_Tag2","RECO_TTH_HAD_PTH_120_200_Tag3","RECO_TTH_HAD_PTH_200_300_Tag0","RECO_TTH_HAD_PTH_200_300_Tag1","RECO_TTH_HAD_PTH_200_300_Tag2","RECO_TTH_HAD_PTH_60_120_Tag0","RECO_TTH_HAD_PTH_60_120_Tag1","RECO_TTH_HAD_PTH_60_120_Tag2","RECO_TTH_HAD_PTH_GT300_Tag0","RECO_TTH_HAD_PTH_GT300_Tag1","RECO_TTH_LEP_PTH_0_60_Tag0","RECO_TTH_LEP_PTH_0_60_Tag1","RECO_TTH_LEP_PTH_0_60_Tag2","RECO_TTH_LEP_PTH_120_200_Tag0","RECO_TTH_LEP_PTH_120_200_Tag1","RECO_TTH_LEP_PTH_200_300_Tag0","RECO_TTH_LEP_PTH_60_120_Tag0","RECO_TTH_LEP_PTH_60_120_Tag1","RECO_TTH_LEP_PTH_60_120_Tag2","RECO_TTH_LEP_PTH_GT300_Tag0","RECO_VBFLIKEGGH_Tag0","RECO_VBFLIKEGGH_Tag1","RECO_VBFTOPO_ACGGH_Tag0","RECO_VBFTOPO_ACGGH_Tag1","RECO_VBFTOPO_ACVBFBSM_Tag0","RECO_VBFTOPO_ACVBFBSM_Tag1","RECO_VBFTOPO_ACVBFSM_Tag0","RECO_VBFTOPO_VHHAD_Tag0","RECO_VBFTOPO_VHHAD_Tag1","RECO_VH_MET_Tag0","RECO_VH_MET_Tag1","RECO_VH_MET_Tag2","RECO_WH_LEP_PTV_0_75_Tag0","RECO_WH_LEP_PTV_0_75_Tag1","RECO_WH_LEP_PTV_75_150_Tag0","RECO_WH_LEP_PTV_75_150_Tag1","RECO_WH_LEP_PTV_GT150_Tag0","RECO_ZH_LEP_Tag0","RECO_ZH_LEP_Tag1"]

for fit in fits:
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "--> Fit type: ",fit
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"    
    base = "yields_{ext}_{fit}".format(ext=ext,fit=fit)
    for cat in allcats:
        fname = "yields_{ext}_{fit}/{cat}.pkl".format(ext=ext,fit=fit,cat=cat)
        if not access(fname,F_OK):
            print "File ",fname," not present!"
    print "\n\n"

        
