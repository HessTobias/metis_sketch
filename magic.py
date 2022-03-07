from records import *


REC_str2fnc = {
    # Information about the STDF file
    "FAR": FAR.FAR,
    "ATR": ATR.ATR,
    # Data collected on a per lot basis
    "MIR": MIR.MIR,
    "MRR": MRR.MRR,
    "PCR": PCR.PCR,
    "HBR": HBR.HBR,
    "SBR": SBR.SBR,
    "PMR": PMR.PMR,
    "PGR": PGR.PGR,
    # "PLR": PLR,
    # "RDR": RDR,
    "SDR": SDR.SDR,
    # Data collected per wafer
    "WIR": WIR.WIR,
    "WRR": WRR.WRR,
    "WCR": WCR.WCR,
    # Data collected on a per part basis
    "PIR": PIR.PIR,
    "PRR": PRR.PRR,
    # Data collected per test in the test program
    "TSR": TSR.TSR,
    # Data collected per test execution
    "PTR": PTR.PTR,
    # "MPR": MPR,
    # "FTR": FTR,
    # Data collected per program segment
    "BPS": BPS.BPS,
    "EPS": EPS.EPS,
    # Generic Data
    "GDR": GDR.GDR,
    "DTR": DTR.DTR,
}
