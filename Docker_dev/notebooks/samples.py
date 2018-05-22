LUMI = 35900 # in pb
#LUMI = 3.5
###
BASE       = 'NANO_Prod/'

####
samples = {    
    'SingleMuon' : {
        'filename' : 'SingleMuonRun2016C-03Feb2017-v1.root',   
        'xsec'     : None,   
        'eff'      : 1.,   
        'kfactor'  : 1.,   
        'weight'   : 1.,   
        'color'    : 'black',   
    },
    'DYJetsToLL' : {
        'filename' : 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1-v2.root',   
        'xsec'     : 3.*1921.8,   
        'eff'      : 1.,   
        'kfactor'  : 1.,   
        'weight'   : 1.,   
        'color'    : 'green',   
    },
    'TT' : {
        'filename' : 'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-v1.root',   
        'xsec'     : 831.76,   
        'eff'      : 1.,   
        'kfactor'  : 1.,   
        'weight'   : 1.,   
        'color'    : 'gold',   
    },
    'WW' : {
        'filename' : 'WW_TuneCUETP8M1_13TeV-pythia8-v1.root',   
        'xsec'     : 118.7,   
        'eff'      : 1.,   
        'kfactor'  : 1.,   
        'weight'   : 1.,   
        'color'    : 'blue',   
    },
    'WZ' : {
        'filename' : 'WZ_TuneCUETP8M1_13TeV-pythia8-v1.root',   
        'xsec'     : 47.2,   
        'eff'      : 1.,   
        'kfactor'  : 1.,   
        'weight'   : 1.,   
        'color'    : 'cyan',   
    },
    'ZZ' : {
        'filename' : 'ZZ_TuneCUETP8M1_13TeV-pythia8-v1.root',   
        'xsec'     : 16.6,   
        'eff'      : 1.,   
        'kfactor'  : 1.,   
        'weight'   : 1.,   
        'color'    : 'red',   
    },   
}
