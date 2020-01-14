# Script name: pullRawKntsFunc.py
# Purpose: Pull raw knts from .xml and returns array with xsec
# all added up
#
# Pueh Leng Tan, 17 Dec 2018

def pullRawKntsFunc2(fName, chType, nuType, tgtType):
    import matplotlib.pyplot as plt
    import scipy.interpolate as itp
    import numpy as np
    import xml.etree.cElementTree as ET
    import pdb
    import sys # For adding paths

    chkList = [chType, tgtType, 'nu:%s' % (str(nuType))]
    myTree = ET.parse(fName)
    myRoot = myTree.getroot()

    eBag = []
    xsBag = []
    nameBag = []
    minBag = []
    maxBag = []
    for spl in myRoot: # for each spline in xml file
        splName = spl.get('name')

        # Achtung: boo is empty if all strings in chkList are found in splName
        boo = list(filter(lambda x: x not in splName, chkList))
        if len(boo)!=0:
            continue

        eTmpBag = []
        xsTmpBag = []

        for knt in spl: # for each knot in spline
            eTmpBag.append(float(knt[0].text))
            xsTmpBag.append(float(knt[1].text))
        eBag.append(eTmpBag)

        xsBag.append(xsTmpBag)
        minBag.append(eTmpBag[0])
        maxBag.append(eTmpBag[-1])
        nameBag.append(splName)

## Interpolation, so that I can add the xsec up
    eMin_GeV = max(minBag)
    eMax_GeV = min(maxBag)
    nEBins = 200
    eLog = np.linspace(np.log10(eMin_GeV), np.log10(eMax_GeV), nEBins)
    eListFine_GeV = 10**eLog

    [nSpl, nKnts] = np.shape(eBag)
    xsItpBag = []
    for iSpl in range(0, nSpl):
        xsItpFunc = itp.interp1d(eBag[iSpl], xsBag[iSpl], kind='linear')
        xsItpBag.append(xsItpFunc(eListFine_GeV))

    totCC = np.sum(xsItpBag, axis=0)

    return [eListFine_GeV, totCC]
