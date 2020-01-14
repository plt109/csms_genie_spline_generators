# Script name: check_my_splines.py
# Purpose: Plotting out cross section from GENIE XML splines to eyeball for
# kinks and rough general sanity checks.
#
# Pueh Leng Tan, 14 Dec 2019

import matplotlib.pyplot as plt
import scipy.interpolate as itp
import numpy as np
import pdb as pdb

from pullRawKntsFunc2 import *
from nu2siFunc import *

fSplineName = 'full_package_conjoined_v9c.xml'
nuType = -16 #-14 #-12 #16 #14 #12

chType = 'NC'
#chType = 'CC'

'''
# O16
tgtType = '1000080160'
nNucleons = 16
#'''

#'''
# H1
tgtType = '1000010010'
nNucleons = 1
#'''

# Pulling cross-section values from .xml file
eGeV = []
xsec = []
fLabel = []
[eGeVTmp, xsecTmp] = pullRawKntsFunc2(fSplineName, chType, nuType, tgtType) 
eGeV.append(eGeVTmp)
xsec.append(nu2si(xsecTmp)/nNucleons) # in 1e-38 cm2/nuc
fLabel.append(('nu: %i, tgt: %s [%s]' % (nuType, tgtType, chType)))
eGeV = np.squeeze(eGeV)
xsec = np.squeeze(xsec)

# Plotting things out to check for kinks or general weirdness
f1 = plt.figure(1)
ax1 = f1.add_subplot(111)
plt.plot(eGeV, xsec*1e-38, '+-', label=fLabel) # xsec in cm2/nuc

plt.axvspan(min(eGeV), 70., facecolor='grey', alpha=0.2, label='Pure native GENIE')
plt.axvspan(70., 200., facecolor='grey', alpha=0.3, label='Transition')
plt.axvspan(200., max(eGeV), facecolor='grey', alpha=0.4, label='Pure CSMS')

ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel(r'$E_\nu$ [GeV]')
ax1.set_ylabel(r'$\sigma^{%s} [cm^2/nucl.]$' % chType)
ax1.legend(loc='lower right')
ax1.minorticks_on()
ax1.grid(which='major', linestyle=':')
ax1.grid(which='minor', linestyle=':')
f1.show()

