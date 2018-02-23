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

def mean_miss_dataFrame(path=".", execution="", problem="", aux="", missType = ["PAPI_L1_TCM", "PAPI_L2_TCM", "PAPI_L3_TCM"]):
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
        data_DOD = pd.read_csv(path + "/" + problem + "/" + "miss_" + execution + "_" + problem + "_DOD_"+ circuit + aux + ".txt", sep=' ')
        valOOD = 0.0
        valDOD = 0.0
#         print("desvio padrão % " + circuit )
        for i in missType:
            valOOD += data_OOD[i].mean()
            valDOD += data_DOD[i].mean()
#             print(i +" OOD "+ str(data_OOD[i].std() / data_OOD[i].mean() *100) + " %")
#             print(i +" DOD "+ str(data_DOD[i].std() / data_DOD[i].mean() *100) + " %")
        newDF.set_value(circuit, "OOD", valOOD)
        newDF.set_value(circuit, "DOD", valDOD)
#     print(newDF)
    return newDF
