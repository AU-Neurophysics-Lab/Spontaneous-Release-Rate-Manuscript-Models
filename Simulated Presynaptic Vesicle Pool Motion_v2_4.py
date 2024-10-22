# -*- coding: utf-8 -*-
#
# Created: 2024
# @author: Michael Gramlich
#
#--------------------------------------------------------------------#
# This simulation models synaptic vesicle motion within a presynapse #
# The presynapse is modeled spatially as a three-dimensional lattice #
#--------------------------------------------------------------------#

# Note: Lines 84/85 define whether this model is constrained or unconstrained

# Define functions to input
import csv
import string
import math
import cmath
import numpy as np	#import package numpy and give it the designation "np"
import os
import random
from postion_update_subroutine_valt2 import sub_condition3_SV_v2D_1
from postion_update_subroutine_valt2 import sub_condition3_SV_v2D_2
from postion_update_subroutine_valt2 import sub_condition3_SV_v2D_3
from Start_Density_Options_v1 import sub_startpoints_SV_v2D_1
from Start_Density_Options_v1 import sub_startpoints_SV_unconstrained_v2D_1
from Start_Density_Options_v1 import sub_startpoints_SV_v2D_3
from funcs_os import check_make_dir


# Note: Define the version number of the model here. This way, any saved files will have an associated version number 
ver_num = "v2_3"

#--------------------------------------#
#  Generate Folders for Data Storage   #
dir = os.getcwd() + "\\TMP_Output\\"
check_make_dir(dir)
dir = os.getcwd() + "\\TMP_Images\\"
check_make_dir(dir)


#--------------------------------------#
#  Initial Variables and global arrays #

# Variables regulating simulations
N_sims = 100                 # Number of stimulations to run

# Variables for output analysis
Rel_Thresh = 0.002        # The threshold probability that a vesicle release event occurs each time a vesicle hits the membrane
Convert_time = 0.3      # The conversion between time-steps to seconds (i.e. each time-step is equal to the number of seconds given by "Convert_time" variable)
Convert_space = 0.05    # The conversion between lattice sites to microns (i.e. each lattice site is equal to the number of microns given by "Convert_space" variable)

Tol_rel_count = []      # Array to store the total release frequency per simulation
mean_rel_freq = []      # Array to stor mean frequency per condition

    #--------------------------------------#
    #  Location of Output data to save     #
dir = os.getcwd() + "\\TMP_images\\"
dir_output = os.getcwd() + "\\TMP_output\\"

# Variables that are dependent on the simulation
P_size_oneD = 22            # How many lattice sites exist in the x-axis (note this is the axis that does not have release sites)
P_size_oneD_Y = 8           # How many lattice sites exist in the y-axis (note this axis defines the number of release sites as well)

sim_time = 400      # Total time simulation will run
N_vesicles = 50      # Number of vesicles in the current simulation
tmp = 0


for ns in range(0,N_sims):
    # Array of presynapse spatial size

    presynapse_bundle_static2D = [[float(0.0) for x in range(int(P_size_oneD_Y))] for y in range(int(P_size_oneD)) ]	        # Generate "array" to represent presynapse at any specific timepoint
    vesicle_time_bundle2D_x = [[float(0.0) for x in range(int(sim_time+tmp))] for v in range(int(N_vesicles)*2)]                  # Generate Array that stores the position of each vesicle as a function of time
    vesicle_time_bundle2D_y = [[float(0.0) for x in range(int(sim_time+tmp))] for v in range(int(N_vesicles)*2)]                  # Generate Array that stores the position of each vesicle as a function of time
    surface_hit_count_2D_x = [0,0]        # Counter array to keep track of what vesicles hit the surface and when
    

    start2D = []
    Vel_high2D_x = []
    Vel_high2D_y = []
    startx = 6
    starty = 0
    Barrier_y = 10
        
    
# Define here whether the presynapse modeled is constrained or un-constrained Un-comment the correct sub-function
#    sub_startpoints_SV_unconstrained_v2D_1(Vel_high2D_x, Vel_high2D_y,P_size_oneD, presynapse_bundle_static2D, N_vesicles, startx, starty, start2D, P_size_oneD_Y)
    sub_startpoints_SV_v2D_3(Vel_high2D_x, Vel_high2D_y,P_size_oneD, presynapse_bundle_static2D, N_vesicles, startx, starty, start2D, P_size_oneD_Y)
    
    for q in range(0,(N_vesicles)):

        vesicle_time_bundle2D_x[int(q)][0] = start2D[q][0]
        vesicle_time_bundle2D_y[int(q)][0] = start2D[q][1]

    
    # Populate the initial presynapse vesicle pool distribution
    for q in range(0,(N_vesicles)):
        presynapse_bundle_static2D[int(vesicle_time_bundle2D_x[int(q)][0])][int(vesicle_time_bundle2D_y[int(q)][0])] = q+1


    # Now run the full process
    for t in range(1,sim_time):
        presynapse_bundle_static2D = [[float(0.0) for x in range(int(P_size_oneD_Y))] for y in range(int(P_size_oneD)) ]       # Overwrite bundle so it can be reset

        for q in range(0,(N_vesicles)):
            presynapse_bundle_static2D[int(vesicle_time_bundle2D_x[int(q)][int(t-1)])][int(vesicle_time_bundle2D_y[int(q)][int(t-1)])] = q+1

        

        for q in range(0,(N_vesicles)):
    


#-----------------2D simulation algorithm------------------------------------#
            
            tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
            tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
            if tmp_move_2D_x < 0:
                tmp_move_2D_x = vesicle_time_bundle2D_x[int(q)][int(t-1)]- Vel_high2D_x[q];
            if tmp_move_2D_y < 0:
                tmp_move_2D_y = vesicle_time_bundle2D_y[int(q)][int(t-1)]- Vel_high2D_y[q];

            con1_2D_x = 0
            con2_2D_x = 0
            con1_2D_y = 0
            con2_2D_y = 0


            # If velocity of current vesicle is zero in both directions, then don't move
            if Vel_high2D_x[q] == 0 and Vel_high2D_y[q] == 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[q][int(t-1)] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[q][int(t-1)] + Vel_high2D_y[q])
                
            # If next lattice site is an edge at X
            if tmp_move_2D_x >= (P_size_oneD) or tmp_move_2D_x == 0:
                
                if tmp_move_2D_x <= 0:
                    surface_hit_count_2D_x.append([t, 1])
                    
                con1_2D_x = 1
                Vel_high2D_x[q] = -Vel_high2D_x[q]
                tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )

            # If next lattice site is an edge at Y
            if tmp_move_2D_y >= (P_size_oneD_Y) or tmp_move_2D_y <= 0:
                con1_2D_y = 1
                Vel_high2D_y[q] = -Vel_high2D_y[q]
                tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )



                # If reverse lattice site is also occupied, don't move this time-step
            if con1_2D_x ==1 or con1_2D_y == 1:
                if tmp_move_2D_y >= (P_size_oneD_Y) or tmp_move_2D_y <= 0:
                    tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-2)] )
                if tmp_move_2D_x >= (P_size_oneD) or tmp_move_2D_x <= 0:
                    tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-2)] )
                
                if (presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]  >=  int(1) ) :
                    vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][int(t-1)])
                    vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][int(t-1)])

            # If reverse lattice site is NOT occupied, move this time-step
                if ( presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]  ==  int(0) ) :
                    vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                    vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])





            # If next lattice site is not an edge, 
            if con1_2D_x == 0 and con1_2D_y == 0:
 
                # Find out if the lattice site is occupied by a stationary vesicle
                    ves_tmp = int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)])
                    if ves_tmp > 0:
                # Check if vesicle in lattice site is stationary and flip only the moving vesicle speed
                        if Vel_high2D_x[int(ves_tmp-1)] == 0 and Vel_high2D_y[int(ves_tmp-1)] == 0:
                        # Now go through all lattice site options to see if the vesicle can move into any other lattice site
                            # Condition 1 The moving vesicle has both x and y velocities
                            if Vel_high2D_y[q] != 0 and Vel_high2D_x[q] != 0:
                                sub_condition3_SV_v2D_1(t, q, con1_2D_x, con1_2D_y, Vel_high2D_x, Vel_high2D_y, presynapse_bundle_static2D, vesicle_time_bundle2D_x,vesicle_time_bundle2D_y, tmp_move_2D_x, tmp_move_2D_y, P_size_oneD,P_size_oneD_Y)
                            # Condition 2 The moving vesicle has only x velocities
                            if Vel_high2D_y[q] == 0 and Vel_high2D_x[q] != 0:
                                sub_condition3_SV_v2D_2(t, q, con1_2D_x, con1_2D_y, Vel_high2D_x, Vel_high2D_y, presynapse_bundle_static2D, vesicle_time_bundle2D_x,vesicle_time_bundle2D_y, tmp_move_2D_x, tmp_move_2D_y, P_size_oneD,P_size_oneD_Y)
                            # Condition 3 The moving vesicle has only y velocities
                            if Vel_high2D_y[q] != 0 and Vel_high2D_x[q] == 0:
                                sub_condition3_SV_v2D_3(t, q, con1_2D_x, con1_2D_y, Vel_high2D_x, Vel_high2D_y, presynapse_bundle_static2D, vesicle_time_bundle2D_x,vesicle_time_bundle2D_y, tmp_move_2D_x, tmp_move_2D_y,P_size_oneD,P_size_oneD_Y)


                # OK, now find out if the next lattice site is occupied by a moving vesicle and what to do
                        if Vel_high2D_x[int(ves_tmp-1)] != 0 or Vel_high2D_y[int(ves_tmp-1)] != 0:
                            # Flip the velocity of the vesicle that was just hit
                            Vel_high2D_x[int(ves_tmp-1)] = -Vel_high2D_x[int(ves_tmp-1)]
                            Vel_high2D_y[int(ves_tmp-1)] = -Vel_high2D_y[int(ves_tmp-1)]
                            # Now go through all lattice site options to see if the vesicle can move into any other lattice site
 # Condition 1 The moving vesicle has both x and y velocities
                            if Vel_high2D_y[q] != 0 and Vel_high2D_x[q] != 0:
                                sub_condition3_SV_v2D_1(t, q, con1_2D_x, con1_2D_y, Vel_high2D_x, Vel_high2D_y, presynapse_bundle_static2D, vesicle_time_bundle2D_x,vesicle_time_bundle2D_y, tmp_move_2D_x, tmp_move_2D_y, P_size_oneD,P_size_oneD_Y)

                            
 # Condition 2 The moving vesicle has only x velocities
                            if Vel_high2D_y[q] == 0 and Vel_high2D_x[q] != 0:
                                sub_condition3_SV_v2D_2(t, q, con1_2D_x, con1_2D_y, Vel_high2D_x, Vel_high2D_y, presynapse_bundle_static2D, vesicle_time_bundle2D_x,vesicle_time_bundle2D_y, tmp_move_2D_x, tmp_move_2D_y, P_size_oneD,P_size_oneD_Y)
 # Condition 3 The moving vesicle has only y velocities
                            if Vel_high2D_y[q] != 0 and Vel_high2D_x[q] == 0:
                                sub_condition3_SV_v2D_3(t, q, con1_2D_x, con1_2D_y, Vel_high2D_x, Vel_high2D_y, presynapse_bundle_static2D, vesicle_time_bundle2D_x,vesicle_time_bundle2D_y, tmp_move_2D_x, tmp_move_2D_y, P_size_oneD,P_size_oneD_Y)


# Final condition where vesicle has already been checked for an edge and a vesicle collision conditon


            # If next lattice x-site is NOT an edge
            if con1_2D_x == 0:
                if tmp_move_2D_x < len(presynapse_bundle_static2D[0]) or tmp_move_2D_x > 0:
                    # If next lattice site is NOT an edge, If lattice site is NOT occupied, move this time-step
                    if (presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]  ==  int(0) ) :
                        vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[q][int(t-1)] + Vel_high2D_x[q])
                    
            # If next lattice y-site is NOT an edge
            if con1_2D_y == 0:
                if tmp_move_2D_y < len(presynapse_bundle_static2D[1]) or tmp_move_2D_y > 0:
           # If next lattice site is NOT an edge, If lattice site is NOT occupied, move this time-step
                   if (presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]  ==  int(0) ) :
                       vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[q][int(t-1)] + Vel_high2D_y[q])


                            
    #--------------- Output current presynapse vesicle pool locations ---------------------#
        if ns == 0:
            current_presyanpse_data = open(dir + "Presynapse_Vesicle_Pool_Distribution_"  + str(N_vesicles)+"_2D"+"_" + ver_num + "_"+str(t)+ ".txt","w")
        
            for i in range(0,P_size_oneD):
                for j in range(0,P_size_oneD_Y):
                    if float(presynapse_bundle_static2D[int(i)][int(j)]) > 0:
                        current_presyanpse_data.write("%f\t" %(float(presynapse_bundle_static2D[int(i)][int(j)]) /float(presynapse_bundle_static2D[int(i)][int(j)]) )   )
                    if float(presynapse_bundle_static2D[int(i)][int(j)])  == 0:
                        current_presyanpse_data.write("%f\t" %(float(presynapse_bundle_static2D[int(i)][int(j)]) )   )
                current_presyanpse_data.write("\n")
        
            current_presyanpse_data.close()
    
    #--------------- ------------------------------------------------ ---------------------#
    
    
    #--------------- Output Final Vesicle Hit counts and release events -------------------#
    Final_presynapse_data = open(dir_output + "Presynapse_Vesicle_ReleaseResults_"  + "N" + str(N_vesicles) + "_V" + str(P_size_oneD) +"_1D_" + "_simN-" + str(ns) + "_ver_num-"+str(ver_num)+" .txt","w")
    tmp_tol_rel = 0
    for i in range(2,len(surface_hit_count_2D_x)):
        tmp_rel = 0       # Reset the temporary release variable
        # Pull an unweighted random number between [0,1] for each hit event and compare to the threshold
        if np.random.rand() < Rel_Thresh:
            tmp_rel = 1
            tmp_tol_rel = tmp_tol_rel + 1
        Final_presynapse_data.write("%f\t%f\t%f\t%f\n" % (float(surface_hit_count_2D_x[int(i)][0]), float(surface_hit_count_2D_x[int(i)][1]), float(surface_hit_count_2D_x[int(i)][0])*Convert_time,float(tmp_rel) )   )
    
    Final_presynapse_data.close()
    Tol_rel_count.append([ns, tmp_tol_rel/sim_time/Convert_time*60])

    mean_rel_freq.append(tmp_tol_rel/sim_time/Convert_time*60)

    #--------------- ------------------------------------------------ ---------------------#
#--------------- Output All Simulation Release Frequencies -------------------#
Final_presynapse_data = open(dir_output + "Presynapse_SimulationResults_"  + "N" + str(N_vesicles) + "_V" + str(P_size_oneD) +"_1D_" + "_ver_num-"+str(ver_num)+" .txt","w")


Final_presynapse_data.write("%f\t%f\t%f\n" % ( np.mean(mean_rel_freq), np.std(mean_rel_freq)/np.sqrt(len(mean_rel_freq)), np.std(mean_rel_freq) )   )
#for i in range(0,len(Tol_rel_count)):
#    Final_presynapse_data.write("%f\t%f\n" % (float(Tol_rel_count[int(i)][0]), float(Tol_rel_count[int(i)][1]) )   )
Final_presynapse_data.close()


Final_vesicle_data_X = open(dir_output + "Vesicle_Position_Results"  + "N" + str(N_vesicles) + "_V" + str(P_size_oneD) +"_1D_" + "_ver_num-"+str(ver_num)+" .txt","w")
for i in range(0,len(vesicle_time_bundle2D_x[1])):
        for j in range(0,len(vesicle_time_bundle2D_x)):
            Final_vesicle_data_X.write("%f\t%f\t" % (vesicle_time_bundle2D_x[j][i], vesicle_time_bundle2D_y[j][i]))
        Final_vesicle_data_X.write("\n")

Final_vesicle_data_X.close()

Final_vesicle_displacemnet = open(dir_output + "Vesicle_Displacement_Results"  + "N" + str(N_vesicles) + "_V" + str(P_size_oneD) +"_1D_" + "_ver_num-"+str(ver_num)+" .txt","w")
for i in range(0,len(vesicle_time_bundle2D_x[1])):
        for j in range(0,len(vesicle_time_bundle2D_x)):
            tmp = np.sqrt((vesicle_time_bundle2D_x[j][i]-vesicle_time_bundle2D_x[j][0])**2 + (vesicle_time_bundle2D_y[j][i] - vesicle_time_bundle2D_y[j][0])**2)
            Final_vesicle_displacemnet.write("%f\t" % (tmp) )
        Final_vesicle_displacemnet.write("\n")

Final_vesicle_displacemnet.close()

Final_vesicle_speed = open(dir_output + "Vesicle_speed_Results"  + "N" + str(N_vesicles) + "_V" + str(P_size_oneD) +"_1D_" + "_ver_num-"+str(ver_num)+" .txt","w")
for i in range(1,len(vesicle_time_bundle2D_x[1])):
        for j in range(0,len(vesicle_time_bundle2D_x)):
            tmp = np.sqrt((vesicle_time_bundle2D_x[j][i]-vesicle_time_bundle2D_x[j][int(i-1)])**2 + (vesicle_time_bundle2D_y[j][i] - vesicle_time_bundle2D_y[j][int(i-1)])**2)
            Final_vesicle_speed.write("%f\t" % (tmp) )
        Final_vesicle_speed.write("\n")

Final_vesicle_speed.close()


    
    
    
    
    