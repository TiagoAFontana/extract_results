# -*- coding: utf-8 -*-
from extract_miss import *
from extract_runtime import *

# iccad2015_circuits = ["superblue18"]

def mean_miss_dataFrame_P3_size(path=".", execution="", problem="", aux="", missType = ["PAPI_L1_TCM", "PAPI_L2_TCM", "PAPI_L3_TCM"], extraSize=["_e25", "_e50", "_e75", "_e100", "_e150", "_e200", "e_400", "e_600"]):
    PAPI = 'PAPI_' + execution +"_"+ problem
#     missType = ["PAPI_L1_DCM", "PAPI_L1_ICM", "PAPI_L1_TCM", "PAPI_L2_DCM", "PAPI_L2_ICM", "PAPI_L2_TCM", "PAPI_L3_TCM"]
#     missType = ["PAPI_L1_TCM", "PAPI_L2_TCM", "PAPI_L3_TCM"]
#     missType = ["PAPI_L1_DCM", "PAPI_L2_DCM", "PAPI_L3_TCM"]

    newDF = pd.DataFrame() #creates a new dataframe that's empty
    newDF = pd.DataFrame(  {PAPI: [] })
    newDF[PAPI] = ["superblue18", "superblue4", "superblue16", "superblue5", "superblue1", "superblue3", "superblue10", "superblue7"]
    newDF.set_index(PAPI, drop=True, append=False, inplace=True, verify_integrity=False)

    # create colunns
    newDF.set_value(iccad2015_circuits[0], "OOD", 0)
    newDF.set_value(iccad2015_circuits[0], "DOD", 0)
    for size in extraSize:
        newDF.set_value(iccad2015_circuits[0], "OOD" + size, 0)
    newDF.set_value(iccad2015_circuits[0], "OOD_std", 0)
    newDF.set_value(iccad2015_circuits[0], "DOD_std", 0)
    for size in extraSize:
        newDF.set_value(iccad2015_circuits[0], "OOD_std" + size, 0)
    newDF.set_value(iccad2015_circuits[0], "OOD_ic", 0)
    newDF.set_value(iccad2015_circuits[0], "DOD_ic", 0)
    for size in extraSize:
        newDF.set_value(iccad2015_circuits[0], "OOD_ic" + size, 0)

    # normal
    for circuit in iccad2015_circuits:
        data_OOD = pd.read_csv(path + "/" + problem + "/" + "miss_" + execution + "_" + problem + "_OOD_"+ circuit + "_e0.txt", sep=' ')
        data_DOD = pd.read_csv(path + "/" + problem + "/" + "miss_" + execution + "_" + problem + "_DOD_"+ circuit + "_e0.txt", sep=' ')
        
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
        #intervalo de confianca de cada circuito
        n = len(data_OOD["TOTAL"])
        m, se = np.mean(data_OOD["TOTAL"].values), scipy.stats.sem(data_OOD["TOTAL"].values)
        icOOD = se * sp.stats.t._ppf((1+0.99)/2., n-1)
        n = len(data_DOD["TOTAL"])
        m, se = np.mean(data_DOD["TOTAL"].values), scipy.stats.sem(data_DOD["TOTAL"].values)
        icDOD = se * sp.stats.t._ppf((1+0.99)/2., n-1)
        newDF.set_value(circuit, "OOD_ic", icOOD)
        newDF.set_value(circuit, "DOD_ic", icDOD) 


    # print('obj extend')

    # obj estendidos
    for size in extraSize:
        for circuit in iccad2015_circuits:
            data_OOD = pd.read_csv(path + "/" + problem + "/" + "miss_" + execution + "_" + problem + "_OOD_"+ circuit + size + ".txt", sep=' ')
            
            data_OOD["TOTAL"] = 0
            for i in missType:
                data_OOD["TOTAL"] += data_OOD[i]
                data_DOD["TOTAL"] += data_DOD[i]

            #media das execuções de cada circuito
            newDF.set_value(circuit, "OOD" + size, data_OOD["TOTAL"].mean())
            
            # desvio das execuções de cada circuito
            newDF.set_value(circuit, "OOD_std" + size, data_OOD["TOTAL"].std())
            
            #intervalo de confianca de cada circuito
            n = len(data_OOD["TOTAL"])
            m, se = np.mean(data_OOD["TOTAL"].values), scipy.stats.sem(data_OOD["TOTAL"].values)
            icOOD = se * sp.stats.t._ppf((1+0.99)/2., n-1)
            newDF.set_value(circuit, "OOD_ic" + size, icOOD)
 
    return newDF

def mean_runtime_dataFrame_P3_size(path=".", execution="", problem="", aux="", extraSize=["_e125", "_e150", "_e175", "_e200", "_e400", "_e600"]):
    #get unit 
    circuit = 'superblue18'
    data_DOD = pd.read_csv(path + "/" + problem + "/" + "runtime_" + execution + "_" + problem + "_DOD_" + ordered + circuit + aux + ".txt", sep=' ')
    unit = data_DOD["unidade"][0]

    RUNTIME = "Runtime" +"_"+ execution +"_"+ problem+"_("+unit+")"

    newDF = pd.DataFrame() #creates a new dataframe that's empty
    newDF = pd.DataFrame(  {RUNTIME: [] })
    newDF[RUNTIME] = ["superblue18", "superblue4", "superblue16", "superblue5", "superblue1", "superblue3", "superblue10", "superblue7"]
    newDF.set_index(RUNTIME, drop=True, append=False, inplace=True, verify_integrity=False)

    for circuit in iccad2015_circuits:
        data_OOD = pd.read_csv(path + "/" + problem + "/" + "runtime_" + execution + "_" + problem + "_OOD_"+ circuit + ".txt", sep=' ')
        data_DOD = pd.read_csv(path + "/" + problem + "/" + "runtime_" + execution + "_" + problem + "_DOD_" + ordered + circuit + aux + ".txt", sep=' ')
        newDF.set_value(circuit, "OOD" + execution, data_OOD["runtime"].mean())
        newDF.set_value(circuit, "DOD" + execution, data_DOD["runtime"].mean())
        newDF.set_value(circuit, "OOD_std" + execution, data_OOD["runtime"].std())
        newDF.set_value(circuit, "DOD_std" + execution, data_DOD["runtime"].std())
#         print("desvio padrão  %" + circuit +" "+ str(data_OOD["runtime"].std() \/ data_OOD["runtime"].mean() *100) + " %")
#         print("desvio padrão  %" + circuit +" "+ str(data_DOD["runtime"].std() \/ data_DOD["runtime"].mean() *100) + " %")
#         print("\n\n")
        
        #intervalo de confianca de cada circuito
        n = len(data_OOD["runtime"])
        m, se = np.mean(data_OOD["runtime"].values), scipy.stats.sem(data_OOD["runtime"].values)
        icOOD = se * sp.stats.t._ppf((1+0.99)/2., n-1)
        n = len(data_DOD["runtime"])
        m, se = np.mean(data_DOD["runtime"].values), scipy.stats.sem(data_DOD["runtime"].values)
        icDOD = se * sp.stats.t._ppf((1+0.99)/2., n-1)
        newDF.set_value(circuit, "OOD_ic", icOOD)
        newDF.set_value(circuit, "DOD_ic", icDOD)


#     print(newDF)

    for circuit in iccad2015_circuits:
        # relação entre DOD e OOD "1-(DOD/OOD)"
        OOD = newDF.get_value(circuit, "OOD"+ execution)
        DOD = newDF.get_value(circuit, "DOD"+ execution)
        newDF.set_value(circuit, "1-(DOD/OOD)", 1-(DOD/OOD))

    # # relação média entre DOD e OOD
    newDF.set_value(iccad2015_circuits[-1], "", newDF["1-(DOD/OOD)"].mean())
    
    # media de todos os circuitos
    # mediaOOD = newDF["OOD"+ execution].mean()
    # mediaDOD = newDF["DOD"+ execution].mean()
    # newDF.set_value(iccad2015_circuits[-1], "mean_OOD", mediaOOD)
    # newDF.set_value(iccad2015_circuits[-1], "mean_DOD", mediaDOD)

    return newDF

def contract_results_P3Psize(path=".", problem="problem3", aux="", out_path='.', miss=True, runtime=True, sequential=True, parallel=True):
    # contract results in one CSV

    fileName = out_path + "/" + problem  + aux + ".csv"
    if miss and sequential:
        dfMissSequential = mean_miss_dataFrame_P3_size(path, "sequential", problem, extraSize=[ "_e125", "_e150", "_e175", "_e200", "_e400", "_e600"])
    if miss and parallel:
        dfMissParallel = mean_miss_dataFrame_P3_size(path, "parallel", problem, extraSize=["_e125", "_e150", "_e175", "_e200", "_e400", "_e600"])
    if runtime and sequential:
        dfRuntimeSequential = mean_runtime_dataFrame_P3_size(path, "sequential", problem, extraSize=["_e125", "_e150", "_e175", "_e200", "_e400", "_e600"])
    if runtime and parallel:
        dfRuntimeParallel = mean_runtime_dataFrame_P3_size(path, "parallel", problem, extraSize=["_e125", "_e150", "_e175", "_e200", "_e400", "_e600"])

    if miss and sequential:
        dfMissSequential.to_csv(fileName, mode='w')
        # with open(fileName, 'a') as outfile:
            # outfile.write('\n')
    if runtime and sequential:
        dfRuntimeSequential.to_csv(fileName, mode='w')
        # with open(fileName, 'a') as outfile:
            # outfile.write('\n')
    if miss and parallel:
        dfMissParallel.to_csv(fileName, mode='w')
        # with open(fileName, 'a') as outfile:
            # outfile.write('\n')
    if runtime and parallel:
        dfRuntimeParallel.to_csv(fileName, mode='w')
        # with open(fileName, 'a') as outfile:
            # outfile.write('\n')

    print("write csv on " + fileName)


path = '/home/tiago/Dropbox/mestrado/experiments/0309_cold_cache_o0_30/O0/problem3_size'
out_path = path + '/csv'
#------------------#
problem3Size = True
#
runtime = True
miss = False
#------------------#
if (problem3Size and miss):
    # Miss Sequential Problem 3
    if miss: contract_results_P3Psize(path, "problem3", "_miss_sequential", out_path, True, False, True, False)
    # Miss Parallel Problem 3
    if miss: contract_results_P3Psize(path, "problem3", "_miss_parallel", out_path, True, False, False, True)
    # Runtime Sequential Problem 3
    if runtime: contract_results_P3Psize(path, "problem3", "_runtime_sequential", out_path, False, True, True, False)
    # Runtime Paralel Problem 3
    if runtime: contract_results_P3Psize(path, "problem3", "_runtime_parallel", out_path,  False, True, False, True)