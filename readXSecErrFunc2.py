# Function name: readXSecErrFunc2.py 
# Purpose: Reads in CSMS xsec files 
#
# Copied from /Users/peaelle42/Documents/iceship/codes/prompt_event_rate/csms_xsec/readXSecErrFunc.py
# Pueh Leng Tan, 14 Jan 2019

def readXSecErrFunc2(fName):
    import numpy as np
    
    E = []
    xSec = []
    upPer = []
    downPer = []

    with open(fName) as tFile:
        for line in tFile:
            tmp = line.split()
            E.append(float(tmp[0]))
            xSec.append(float(tmp[1]))
            upPer.append(float(tmp[2]))
            downPer.append(float(tmp[3]))

    E = np.asarray(E)
    xSec = np.asarray(xSec)
    upPer = np.asarray(upPer)
    downPer = np.asarray(downPer)

    up = xSec*(upPer/100+1)
    down = xSec*(downPer/100+1)

    return [E, xSec, up, down]
