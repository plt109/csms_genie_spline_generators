# Function name: nu2siFunc.py
# Purpose: Converts cross-section from Natural Units (GeV-2) to SI Units (cm2).
# Cross-section in GENIE splines.xml are in Natural Units while cross-section in
# GENIE event.root are in SI Units but in 1e-38cm2, see Section 7.7 on pg 122 of
# 1510.05494 GENIE documentation for details
#
# Pueh Leng Tan, 28 June 2018

def nu2si(xsec_nu):
    xsec_si = xsec_nu*(1e12)/(5.07*5.07) # in 1e-38 cm2
    return xsec_si

