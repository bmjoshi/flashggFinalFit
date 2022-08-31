python RunText2Workspace.py --ext CP --mode mu_simple_sm --batch local

# fit with all other mu's floating (simple combine command)
combine -M MultiDimFit -m 125 -d Datacard_sm_mu_simple.root --floatOtherPOIs 1 -t -1 -n _profile1D_syst_r_VBF_exp -P r_VBF --algo grid --points 40 --alignEdges 1 --setParameters r_ggH=1,r_top=1,r_VH=1 --setParameterRanges r_VBF=0,3 --saveSpecifiedNuis all --saveInactivePOI 1 --freezeParameters MH --cminDefaultMinimizerStrategy 0 --autoBoundsPOIs "*" --autoMaxPOIs "*" --fastScan
plot1DScan.py higgsCombine_profile1D_syst_r_VBF_exp.MultiDimFit.mH125.root --y-cut 40 --y-max 40 --output plots/fits2022-08-30_mu/scan_r_VBF_exp --POI r_VBF --logo-sub "Super-Preliminary"

# or with the RunFits automatic tool
python RunFits.py --inputJson inputs.json --mode sm_mu_simple --batch local [--doObserved]

# then plot the scans and save the best fits
python PlotScans.py --inputJson inputs.json --mode sm_mu_simple --outdir 2022-08-31-fits [--doObserved]




### CP part
python RunText2Workspace.py --ext CP --mode cp           --batch local

# this floats mu, so x (f_CP) is not relevant
combine -M MultiDimFit -m 125 -d DatacardCP_cp.root --floatOtherPOIs 1 -t -1 -n _profile1D_syst_r -P r --algo grid --points 40 --alignEdges 1 --setParameters r=1 --setParameterRanges r=0,2 --saveSpecifiedNuis all --saveInactivePOI 1 --cminApproxPreFitTolerance=10 --freezeParameters MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2

plot1DScan.py higgsCombine_profile1D_syst_r.MultiDimFit.mH125.root --y-cut 40 --y-max 40 --output plots/fits2022-04-28_run2_CP/output_mu_inclusive --POI r --translate ../Plots/pois_cp.json --logo-sub "Preliminary"

# this fits only f_CP, floating the global mu
combine -M MultiDimFit -m 125 -d DatacardCP_cp.root -t -1 -n _profile1D_syst_cp --algo grid --points 20 --alignEdges 1 --setParameters r=1 --setParameterRanges r=0,1 --saveSpecifiedNuis all --freezeParameters MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints

plot1DScan.py higgsCombine_profile1D_syst_cp.MultiDimFit.mH125.root --y-cut 60 --y-max 60 --output plots/fits2022-04-28_run2_CP/output_fcp --POI x --translate ../Plots/pois_cp.json --logo-sub "Preliminary"
