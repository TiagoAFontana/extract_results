# -*- coding: utf-8 -*-
iccad2015_circuits = ["superblue18", "superblue4", "superblue16", "superblue5", "superblue1", "superblue3", "superblue10", "superblue7"]
# iccad2015_circuits = ["superblue5"]

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from os import listdir
from os.path import isfile, join

def runtime_dataFrame(path=".", execution="", problem="", aux=""):
    newDF = pd.DataFrame() #creates a new dataframe that's empty
    newDF = pd.DataFrame( {"Runtime(us)": [] })
    newDF["Runtime(us)"] = ["sequential", "parallel"]
    newDF.set_index("Runtime(us)", drop=True, append=False, inplace=True, verify_integrity=False)
    for circuit in iccad2015_circuits:
        data_OOD = pd.read_csv(path +  "/" + "runtime_" + execution + "_" + problem + "_OOD_"+ circuit + ".txt", sep=' ')
        data_DOD = pd.read_csv(path +  "/" + "runtime_" + execution + "_" + problem + "_DOD_"+ circuit + aux + ".txt", sep=' ')
        newDF[circuit+"_OOD"] = [data_OOD["runtime"].mean() ]
        newDF[circuit+"_DOD"] = [data_DOD["runtime"].mean() ]
    return newDF

def mean_runtime_dataFrame(path=".", execution="", problem="", aux=""):
    RUNTIME = "Runtime"+execution +"_"+ problem+"_(us)"

    newDF = pd.DataFrame() #creates a new dataframe that's empty
    newDF = pd.DataFrame(  {RUNTIME: [] })
    newDF[RUNTIME] = ["superblue18", "superblue4", "superblue16", "superblue5", "superblue1", "superblue3", "superblue10", "superblue7"]
    newDF.set_index(RUNTIME, drop=True, append=False, inplace=True, verify_integrity=False)

    for circuit in iccad2015_circuits:
        data_OOD = pd.read_csv(path + "/" + problem + "/" + "runtime_" + execution + "_" + problem + "_OOD_"+ circuit + ".txt", sep=' ')
        data_DOD = pd.read_csv(path + "/" + problem + "/" + "runtime_" + execution + "_" + problem + "_DOD_"+ circuit + aux + ".txt", sep=' ')
        newDF.set_value(circuit, "OOD" + execution, data_OOD["runtime"].mean())
        newDF.set_value(circuit, "DOD" + execution, data_DOD["runtime"].mean())
#         print("desvio padrão  %" + circuit +" "+ str(data_OOD["runtime"].std() \/ data_OOD["runtime"].mean() *100) + " %")
#         print("desvio padrão  %" + circuit +" "+ str(data_DOD["runtime"].std() \/ data_DOD["runtime"].mean() *100) + " %")
#         print("\n\n")
#     print(newDF)
    return newDF
