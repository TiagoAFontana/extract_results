iccad2015_circuits = ["superblue18", "superblue4", "superblue16", "superblue5", "superblue1", "superblue3", "superblue10", "superblue7"]
# iccad2015_circuits = ["superblue5"]

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from os import listdir
from os.path import isfile, join

def miss_dataFrame(path=".", execution="", problem="", aux=""):
    PAPI = 'PAPI_' + execution
    newDF = pd.DataFrame() #creates a new dataframe that's empty
    newDF = pd.DataFrame( {PAPI: []})
    newDF[PAPI] = ["PAPI_L1_DCM", "PAPI_L1_ICM", "PAPI_L1_TCM", "PAPI_L2_DCM", "PAPI_L2_ICM", "PAPI_L2_TCM", "PAPI_L3_TCM"]
    newDF.set_index(PAPI, drop=True, append=False, inplace=True, verify_integrity=False)
    for circuit in iccad2015_circuits:
        data_OOD = pd.read_csv(path + "/" + "miss_" + execution + "_" + problem + "_OOD_"+ circuit + ".txt", sep=' ')
        data_DOD = pd.read_csv(path + "/" + "miss_" + execution + "_" + problem + "_DOD_"+ circuit + aux + ".txt", sep=' ')
        newDF[circuit+"_OOD"] = [data_OOD["PAPI_L1_DCM"].mean(), data_OOD["PAPI_L1_ICM"].mean(), data_OOD["PAPI_L1_TCM"].mean(), data_OOD["PAPI_L2_DCM"].mean(), data_OOD["PAPI_L2_ICM"].mean(), data_OOD["PAPI_L2_TCM"].mean(), data_OOD["PAPI_L3_TCM"].mean() ]
        newDF[circuit+"_DOD"] = [data_DOD["PAPI_L1_DCM"].mean(), data_DOD["PAPI_L1_ICM"].mean(), data_DOD["PAPI_L1_TCM"].mean(), data_DOD["PAPI_L2_DCM"].mean(), data_DOD["PAPI_L2_ICM"].mean(), data_DOD["PAPI_L2_TCM"].mean(), data_DOD["PAPI_L3_TCM"].mean() ]
#     print(newDF)
#     newDF.to_csv(problem + "_miss_"+ technique + "_" + execution + aux +".csv")
#     newDF.to_csv(path+"/outPAPI.csv")
#     print("CSV generated! -> (" + path + "/outPAPI.csv)")
    return newDF

def mean_miss_dataFrame(path=".", execution="", problem="", aux="", missType = ["PAPI_L1_TCM", "PAPI_L2_TCM", "PAPI_L3_TCM"], ordered=""):
    PAPI = 'PAPI_' + execution +"_"+ problem
#     missType = ["PAPI_L1_DCM", "PAPI_L1_ICM", "PAPI_L1_TCM", "PAPI_L2_DCM", "PAPI_L2_ICM", "PAPI_L2_TCM", "PAPI_L3_TCM"]
#     missType = ["PAPI_L1_TCM", "PAPI_L2_TCM", "PAPI_L3_TCM"]
#     missType = ["PAPI_L1_DCM", "PAPI_L2_DCM", "PAPI_L3_TCM"]

    newDF = pd.DataFrame() #creates a new dataframe that's empty
    newDF = pd.DataFrame(  {PAPI: [] })
    newDF[PAPI] = ["superblue18", "superblue4", "superblue16", "superblue5", "superblue1", "superblue3", "superblue10", "superblue7"]
    newDF.set_index(PAPI, drop=True, append=False, inplace=True, verify_integrity=False)

    for circuit in iccad2015_circuits:
        data_OOD = pd.read_csv(path + "/" + problem + "/" + "miss_" + execution + "_" + problem + "_OOD_"+ circuit + ".txt", sep=' ')
        data_DOD = pd.read_csv(path + "/" + problem + "/" + "miss_" + execution + "_" + problem + "_DOD_"+ ordered + circuit + aux + ".txt", sep=' ')
        
        data_OOD["TOTAL"] = 0
        data_DOD["TOTAL"] = 0
        for i in missType:
            data_OOD["TOTAL"] += data_OOD[i]
            data_DOD["TOTAL"] += data_DOD[i]

        #media das execuções de cada circuito
        newDF.set_value(circuit, "OOD", data_OOD["TOTAL"].mean())
        newDF.set_value(circuit, "DOD", data_DOD["TOTAL"].mean())
        # desvio das execuções de cada circuito
        newDF.set_value(circuit, "OOD_std", data_OOD["TOTAL"].std())
        newDF.set_value(circuit, "DOD_std", data_DOD["TOTAL"].std())  
    
    for circuit in iccad2015_circuits:
        # relação entre DOD e OOD "1-(DOD/OOD)"
        OOD = newDF.get_value(circuit, "OOD")
        DOD = newDF.get_value(circuit, "DOD")
        newDF.set_value(circuit, "1-(DOD/OOD)", 1-(DOD/OOD))

    # # relação média entre DOD e OOD
    newDF.set_value(iccad2015_circuits[-1], "", newDF["1-(DOD/OOD)"].mean())
    
    # media de todos os circuitos
    # mediaOOD = newDF["OOD"].mean()
    # mediaDOD = newDF["DOD"].mean()
    # newDF.set_value(iccad2015_circuits[-1], "mean_OOD", mediaOOD)
    # newDF.set_value(iccad2015_circuits[-1], "mean_DOD", mediaDOD)
    
    # print(newDF)
    return newDF
