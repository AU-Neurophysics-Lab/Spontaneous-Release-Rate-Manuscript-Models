# This code will take the experimental intensity profiles and fit them to 
# the simulated intensity database prefiles to determine the optimal fit


import csv
import string
import math
import cmath
import numpy as np	#import package numpy and give it the designation "np"
import os
import random
from funcs_os import check_make_dir




N_syns = 100
Stim_end = 200
P_site = 0.01
P_decay_start = 2
P_decay = 20
P_max = 2.0
T_end_start = 200
Stim_per_frame = 4
ver_num = "v4_1d"

Exp_start = 900
Exp_Int_scale = 2000

# Define the parameters of the experimental data here

Intensity_per_vesicle = 450         # Define the intensity per vesicle
N_exp_syns = 752                    # Define the number of synapses in the experimental dataset
Fname = "_7523_P2B1"                # Define the filename of the experimental dataset


CHI_all = []

Num_headers = 3
Total_params_out = []

for q in range(1,(1+N_exp_syns)):
    CHI_min = 0
    N_min = 0
    Start_min = 0 
    End_min = 0 
    Pool_min = 0 
    Release_max = 0 
    End_min = 0 
    E_X = []
    test_data = open(os.getcwd() + "\\" + "tmp_combined" + Fname + ".txt","r")

    t_tmp = []
    y1 = []
    for qq in range(0,Num_headers): 
        r = test_data.readline()   # Assume first row is header to read and ignore
        cols = r.split()
        E_X.append(float(cols[q]))
        
    while True:
        r = test_data.readline()

        cols = r.split()
        if len(cols) >0 : 
            y1.append(float(cols[q]))
            t_tmp.append(float(cols[0]))

        if not r: break
    test_data.close()
    Exp_Int_scale = np.mean( y1[int(Exp_start):int(Exp_start+100)] )

    
    for N_release_sites in range(1,21):
        for Stim_start in range(100, 295,5):
            for Stim_end in range((Stim_start+15), 195,5):
                for T_end_start in range(200, 250,25):
    
                    dir = os.getcwd() + "\\Synapse Data\\Intensity_per_vesicle_"+ str(Intensity_per_vesicle)
                    new_dir = dir +  "\\" + str(N_syns) +"_" + str(N_release_sites) +"_" + str(Intensity_per_vesicle) +"_" + str(Stim_per_frame) +"_" + str(Stim_start) +"_" + str(Stim_end) +"_" + str(P_decay_start) +"_" + str(P_site) +"_" + str(P_max) +"_" + str(P_decay) +"_" + str(T_end_start) + "\\"
                    all_data_combined_out = open(new_dir + "all_synapsedata"  + str(N_syns) +"_" + str(N_release_sites) +"_" + str(Intensity_per_vesicle) +"_" + str(Stim_per_frame) +"_" + str(Stim_start) +"_" + str(Stim_end) +"_" + str(P_decay_start) +"_" + str(P_site) +"_" + str(P_max) +"_" + str(P_decay) +"_" + str(T_end_start) +"_" + "-v_" + ver_num + ".txt","r")
                    t_tmp2 = []
                    y2 = []
                    Release_tmp = []
                    Pool_size = []
                    
                    for qq in range(1,Num_headers): 
                        r =  all_data_combined_out.readline()   # Assume first row(s) are header to read and ignore
                        
                    while True:
                        r =  all_data_combined_out.readline()
                        cols = r.split()
                        if len(cols) >0 : 
                            y2.append(float(cols[1]))
                            t_tmp2.append(float(cols[0]))
                            Release_tmp.append(float(cols[2]))
                            Pool_size.append(float(cols[3]))
                        if not r: break
    
                    # Calculate the chi-square number
                    CHI_tmp = 0
                    for ttt in range(100,200):
                        CHI_tmp = CHI_tmp + ((y1[int(ttt)+int(Exp_start)]-(y2[int(ttt)]+Exp_Int_scale))*(y1[int(ttt)+int(Exp_start)]-(y2[int(ttt)]+Exp_Int_scale)))
                    CHI_all.append(CHI_tmp)
                    if CHI_min == 0:
                        CHI_min = CHI_tmp
                    if CHI_min != 0 and (CHI_tmp < CHI_min):
                        CHI_min = CHI_tmp
                        y_min = y2
                        N_min = N_release_sites
                        Start_min = Stim_start
                        End_min = Stim_end
                        Pool_min = np.min(Pool_size)
                        Release_max = np.max(Release_tmp)
                        End_min = T_end_start
                    all_data_combined_out.close()

    tmp_app = [E_X[0], E_X[1],E_X[2], Intensity_per_vesicle, N_min,Start_min ,End_min,P_site, P_decay_start,P_decay,P_max, End_min, Stim_per_frame, Exp_start, Exp_Int_scale, Pool_min, Release_max]
    Total_params_out.append(tmp_app)




# This section outputs the best fit parameters to the experimental dataset on a synapse-by-synapse basis

out_data = open(os.getcwd() + "\\" +"tmp_output" + Fname + ".txt","w")
for q in range(0,N_exp_syns-1):
    out_data.write("%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n" %(Total_params_out[q][0], Total_params_out[q][1], Total_params_out[q][2], Total_params_out[q][3], Total_params_out[q][4], Total_params_out[q][5], Total_params_out[q][6], Total_params_out[q][7], Total_params_out[q][8], Total_params_out[q][9], Total_params_out[q][10], Total_params_out[q][11], Total_params_out[q][12], Total_params_out[q][13], Total_params_out[q][14], Total_params_out[q][15], Total_params_out[q][16]))
out_data.close()


