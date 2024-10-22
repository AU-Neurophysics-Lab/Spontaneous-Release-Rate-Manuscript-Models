


import csv
import string
import math
import cmath
import numpy as np	#import package numpy and give it the designation "np"
import os
import random
import matplotlib.pyplot as plt

from funcs_os import check_make_dir

# Note: Define the version number of the model here
ver_num = "v4_1d"



#--------------------#
#  Initial Variables #

# Variables Independent of Stimulus Change
Sym_length = 700
BKG_start = 1
BKG_end = 1
BKG_decay = 1

M_re_t = 5 # Model Site Re-use instead of P
T_endocytosis = 200
Photobleaching_perframe = 0.9

#-------------------------#
# This section is hard coded in case another round of stimulation was done.
# Second Stimulation Round
Is_Second_Stim = 0;     # 0 = NO, 1 = YES
Stim_per_frame2 = 4
P_site2 = 0.005
P_site_start2 = P_site2*1.7
P_decay2 = 30
T_end_start2 = 300
T_endocytosis2 = 300
Stim_start2 = 300
Stim_end2 = 360


# Initiate the count of vesicles released
Count_ves = 0
tmpN = 0
# Initiate the count of total available vesicles
Count_tot = 100 # What is the total pool size
#--------------------#



####################################################
def generate_sub_model(N_syns, Intensity_per_vesicle, N_release_sites, Stim_start, Stim_end, P_site, P_max,P_decay_start, P_decay,T_end_start, Stim_per_frame):
	P_site_start = P_site*P_max
	Intensity_per_P301L = Intensity_per_vesicle*1.0
	P_P301L_VGLUT1_2 = 1.00
	dir = os.getcwd() + "\\Synapse Data\\"
	new_dir = dir +  "\\" + str(N_syns) +"_" + str(N_release_sites) +"_" + str(Intensity_per_vesicle) +"_" + str(Stim_per_frame) +"_" + str(Stim_start) +"_" + str(Stim_end) +"_" + str(P_decay_start) +"_" + str(P_site) +"_" + str(P_max) +"_" + str(P_decay) +"_" + str(T_end_start) + "\\"
	check_make_dir(new_dir)

#-----------------------------------------------#
#	Initialize bundle lattice		#

	Bundle_size = Sym_length
# Generate Aggregate Array for final results
	aggregate_bundle_static = [[float(0.0) for x in range(int(Bundle_size))] for z in range(0,int(N_syns)+1)]	        # Generate "array" to store bundle data
	aggregate_bundle_PoolSize_static = [[float(0.0) for x in range(int(Bundle_size))] for z in range(0,int(N_syns)+1)]	# Generate "array" to store bundle data
	aggregate_bundle_release_static = [[float(0.0) for x in range(int(Bundle_size))] for z in range(0,int(N_syns)+1)]	# Generate "array" to store bundle data


	all_data_combined_out = open(new_dir + "all_synapsedata"  + str(N_syns) +"_" + str(N_release_sites) +"_" + str(Intensity_per_vesicle) +"_" + str(Stim_per_frame) +"_" + str(Stim_start) +"_" + str(Stim_end) +"_" +
                                 str(P_decay_start) +"_" + str(P_site) +"_" + str(P_max) +"_" + str(P_decay) +"_" + str(T_end_start) +"_" + "-v_" + ver_num + ".txt","w")
	all_paramaters_combined_out = open(new_dir + "all_synapse_paramaters" + str(N_syns) +"_" + str(N_release_sites) +"_" + str(Intensity_per_vesicle) +"_" + str(Stim_per_frame) +"_" + str(Stim_start) +"_" + str(Stim_end) +"_" +
                                 str(P_decay_start) +"_" + str(P_site) +"_" + str(P_max) +"_" + str(P_decay) +"_" + str(T_end_start) +"_" + "-v_" + ver_num + ".txt","w")

# Initialize arrays for stimulation-dependent parameter properties
	p_tmp_trk = []  # Keep track of changning release probability during stimulation
	pulse_tmp_trk = [] # Keep track of number of stimulation pulses
#pulse_tmp_trk.append(0)


# Start the main code with initiation of the number of simulations

	for i in range(1,N_syns):
#		print(i)
		TwoD_Bundle_Distribution_static = [[float(0.0) for x in range(int(Bundle_size))] for z in range(0,int(N_release_sites))]	# Generate "array" to store bundle data
		Bundle_NumVesicles_static = [float(0.0) for x in range(int(Bundle_size))] 	# Generate "array" to store Number of Vesicles Released
		Bundle_PoolSize_static = [float(Count_tot) for x in range(int(Bundle_size))] 	# Generate "array" to store Number of Vesicles in Total Pool
		TwoD_Bundle_Reuse_static = [[float(0.0) for x in range(int(Bundle_size))] for z in range(0,int(N_release_sites))]	# Generate "array" to store if lattice sites have been re-used
		


#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Now run through the simulation and simulate vesicle release events

		P_curr = P_site_start
		for sim in range(0,Bundle_size):
			if i == 1:
				if sim < Stim_start:
					pulse_tmp_trk.append(0)
				if sim > Stim_start:
					if sim < Stim_end:
						pulse_tmp_trk.append(Stim_per_frame)    
				if sim > Stim_end:
						pulse_tmp_trk.append(0)    
	
                    
		# Start By applying a background
			for y in range(0, N_release_sites): TwoD_Bundle_Distribution_static[int(y)][int(sim)] += (BKG_start + BKG_end*(1-np.exp(-(sim)/BKG_decay)))/N_release_sites
			# Limit Range to when stimulation occurs for First Round
			if sim > Stim_start:
				if sim < Stim_end:
				# Control for how many times per frame a stimulation occurs
				
					if i == 1:
							p_tmp_trk.append(P_curr*N_release_sites)
						                    

                
					for stimN in range(0, Stim_per_frame):
						for y in range(0, N_release_sites):
						# Check for previous release
						#if TwoD_Bundle_Distribution_static[int(y)][int(sim-1)] > 0: TwoD_Bundle_Distribution_static[int(y)][int(sim)] += TwoD_Bundle_Distribution_static[int(y)][int(sim-1)]

						# Determine the current release probability based on the stimulation frequency
							Release_prob = np.random.rand()   #Pull a random probability between (0,1)
							P_curr = P_site_start # Model a Single re-use site
							if sim > Stim_start+P_decay_start:
								P_curr = P_site+(P_site_start-P_site)*np.exp(-(sim-Stim_start)/P_decay)
						#print(P_curr)
							if i == 1:
								p_tmp_trk.append(P_curr*N_release_sites)           

						# Determine the number of pulses that has occured in order to determine the current endocytosis rate
							T_endo_curr = T_endocytosis +(T_end_start-T_endocytosis)*np.exp(-(sim-Stim_start)/10)
							Endo_time = (np.random.exponential(T_endo_curr)) #Pull a random number from an exponential distribution for how long the vesicle will stay

        					# Determine the How long the site will wait to be re-used
							Reuse_time = (np.random.exponential(M_re_t)) #Pull a random number from an exponential distribution for how long the site will be silent


						# Determine the number of VGLUT1 copies
							Intensity_prob = np.random.rand()   #Pull a random probability between (0,1)
							if Intensity_prob < P_P301L_VGLUT1_2: Intensity_curr = Intensity_per_P301L
							if Intensity_prob > P_P301L_VGLUT1_2: Intensity_curr = Intensity_per_vesicle
						
							if Release_prob < P_curr and TwoD_Bundle_Reuse_static[int(y)][int(sim)] == 0:
					#TwoD_Bundle_Distribution_static[int(y)][int(sim)] = Endo_time
					# Add the vesicle for the time it has been given until endocytosis
								Bundle_NumVesicles_static[int(sim)] += 1;
								if Endo_time + sim < Bundle_size:
									for tot in range(1,int(Endo_time)):
										TwoD_Bundle_Distribution_static[int(y)][int(tot)+int(sim)] += Intensity_curr
										Bundle_PoolSize_static[int(tot)+int(sim)] += -1
										
	                                        # Now account for re-use time
									for tot in range(1,int(Reuse_time)):
										TwoD_Bundle_Reuse_static[int(y)][int(tot)+int(sim)] += -1
	
									
								if Endo_time + sim > Bundle_size:
									for tot in range(1,int(Bundle_size)-sim): TwoD_Bundle_Distribution_static[int(y)][int(tot)+int(sim)] += Intensity_curr 
				for y in range(0, N_release_sites):
					if TwoD_Bundle_Distribution_static[int(y)][int(sim-1)] > 0: TwoD_Bundle_Distribution_static[int(y)][int(sim)] = TwoD_Bundle_Distribution_static[int(y)][int(sim)]*Photobleaching_perframe 
	

# If there is a Second round of stimulation, run that code here

			if Is_Second_Stim == 1 and sim > Stim_start2:
				if sim < Stim_end2:
				# Control for how many times per frame a stimulation occurs
					for stimN in range(0, Stim_per_frame2):
						for y in range(0, N_release_sites):
						# Check for previous release
						#if TwoD_Bundle_Distribution_static[int(y)][int(sim-1)] > 0: TwoD_Bundle_Distribution_static[int(y)][int(sim)] += TwoD_Bundle_Distribution_static[int(y)][int(sim-1)]
	
							# Determine the current release probability based on the stimulation frequency
							Release_prob = np.random.rand()   #Pull a random probability between (0,1)
							P_curr = P_site2+(P_site_start2-P_site2)*np.exp(-(sim-Stim_start2)/P_decay2)

						# Determine the number of pulses that has occured in order to determine the current endocytosis rate
							T_endo_curr = T_endocytosis2 +(T_end_start2-T_endocytosis2)*np.exp(-(sim-Stim_start2)/10)
							Endo_time = (np.random.exponential(T_endo_curr)) #Pull a random number from an exponential distribution for how long the vesicle will stay

        					# Determine the How long the site will wait to be re-used
							Reuse_time = (np.random.exponential(M_re_t)) #Pull a random number from an exponential distribution for how long the site will be silent


						# Determine the number of VGLUT1 copies
							Intensity_prob = np.random.rand()   #Pull a random probability between (0,1)
							if Intensity_prob < P_P301L_VGLUT1_2: Intensity_curr = Intensity_per_P301L
							if Intensity_prob > P_P301L_VGLUT1_2: Intensity_curr = Intensity_per_vesicle
							
							if Release_prob < P_curr and TwoD_Bundle_Reuse_static[int(y)][int(sim)] == 0:
					#TwoD_Bundle_Distribution_static[int(y)][int(sim)] = Endo_time
					# Add the vesicle for the time it has been given until endocytosis
								Bundle_NumVesicles_static[int(sim)] += 1;
								if Endo_time + sim < Bundle_size:
									for tot in range(1,int(Endo_time)):
										TwoD_Bundle_Distribution_static[int(y)][int(tot)+int(sim)] += Intensity_curr
										Bundle_PoolSize_static[int(tot)+int(sim)] += -1
									
                                        # Now account for re-use time
									for tot in range(1,int(Reuse_time)):
										TwoD_Bundle_Reuse_static[int(y)][int(tot)+int(sim)] += -1

									
								if Endo_time + sim > Bundle_size:
									for tot in range(1,int(Bundle_size)-sim): TwoD_Bundle_Distribution_static[int(y)][int(tot)+int(sim)] += Intensity_curr 
				for y in range(0, N_release_sites):
					if TwoD_Bundle_Distribution_static[int(y)][int(sim-1)] > 0: TwoD_Bundle_Distribution_static[int(y)][int(sim)] = TwoD_Bundle_Distribution_static[int(y)][int(sim)]*Photobleaching_perframe 
	


#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#





#--------------------##--------------------##--------------------##--------------------##--------------------#
# This section is for the output of all simulated data

# Level 1 prints out the raw data
# Level 2 Sums all the synapse contributions per individual simulations
# Level 3 aggregates all simulated synapses


#	synapse_out = open(dir + "rawsynapsedata_" + str(i) + "-v_" + ver_num + ".txt","w")
		Count_ves = 0

		for x in range(0, Bundle_size):
	#		synapse_out.write("%f\t" % (float(x*0.1)) )
			
			tmpp = 0
		
		
			for y in range(0, N_release_sites):
				tmpp += float(TwoD_Bundle_Distribution_static[int(y)][int(x)])
	#			synapse_out.write("%f\t" % (TwoD_Bundle_Distribution_static[int(y)][int(x)]) )
	
	#		synapse_out.write("%f\t%f\t" % (float(x*0.1),float(tmpp)) )
			# Output Data on Number of Vesicles Released
			Count_ves +=  float(Bundle_NumVesicles_static[int(x)])
	#		synapse_out.write("%f\t%f\t%f\t%f\t" % (float(x*0.1),float(Bundle_NumVesicles_static[int(x)]),float(Count_ves),float(Bundle_PoolSize_static[int(x)]) ))
			
			aggregate_bundle_static[int(i)][int(x)] = tmpp
			aggregate_bundle_PoolSize_static[int(i)][int(x)] = Bundle_PoolSize_static[int(x)]
			aggregate_bundle_release_static[int(i)][int(x)] = Count_ves
			
	#		synapse_out.write("\n")	
	
	
# Now Average (mean) the complete data sets

	Intensity_mean = np.mean(aggregate_bundle_static, axis = 0);
	ReleaseNumber_mean = np.mean(aggregate_bundle_release_static, axis = 0);
	PoolSize_mean = np.mean(aggregate_bundle_PoolSize_static, axis = 0);
	
	#print(len(Intensity_mean), len(ReleaseNumber_mean))
	

	#print(PoolSize_mean);

#-----------------------------------------------#
# Now output the simulation paramaters to a file for later comparisons

	all_paramaters_combined_out.write("----------------------------------------\n")
	all_paramaters_combined_out.write("    Background Simulation Parameters   \n")
	all_paramaters_combined_out.write("N_syns = %f\n" % (N_syns))
	all_paramaters_combined_out.write("Sym_length = %f\n" % (Sym_length))
	all_paramaters_combined_out.write("N_release_sites = %f\n" % (N_release_sites))
	all_paramaters_combined_out.write("BKG_start = %f\n" % (BKG_start))
	all_paramaters_combined_out.write("BKG_end = %f\n" % (BKG_end))
	all_paramaters_combined_out.write("BKG_decay = %f\n" % (BKG_decay))
	
	all_paramaters_combined_out.write("Intensity_per_vesicle = %f\n" % (Intensity_per_vesicle))
	all_paramaters_combined_out.write("Intensity_per_P301L = %f\n" % (Intensity_per_P301L))
	all_paramaters_combined_out.write("P_P301L_VGLUT1_2 = %f\n" % (P_P301L_VGLUT1_2))
	# Initiate the count of total available vesicles
	all_paramaters_combined_out.write("Count_tot = %f\n" % (Count_tot))
	
	
	
	all_paramaters_combined_out.write("----------------------------------------\n")
	all_paramaters_combined_out.write(" First Round Of Stimulation Parameters  \n")
	all_paramaters_combined_out.write("M_re_t = %f\n" % (M_re_t))
	all_paramaters_combined_out.write("Stim_per_frame = %f\n" % (Stim_per_frame))
	all_paramaters_combined_out.write("P_decay_start = %f\n" % (P_decay_start))
	all_paramaters_combined_out.write("P_site = %f\n" % (P_site))
	all_paramaters_combined_out.write("P_site_start = %f\n" % (P_site_start))
	all_paramaters_combined_out.write("P_decay = %f\n" % (P_decay))
	all_paramaters_combined_out.write("Stim_start = %f\n" % (Stim_start))
	all_paramaters_combined_out.write("Stim_end = %f\n" % (Stim_end))
	
	all_paramaters_combined_out.write("T_end_start = %f\n" % (T_end_start))
	all_paramaters_combined_out.write("T_endocytosis = %f\n" % (T_endocytosis))
	all_paramaters_combined_out.write("Photobleaching_perframe = %f\n" % (Photobleaching_perframe))
	
	# Second Stimulation Round
	all_paramaters_combined_out.write("----------------------------------------\n")
	all_paramaters_combined_out.write(" Second Round Of Stimulation Parameters \n")
	if Is_Second_Stim == 0:
		all_paramaters_combined_out.write(" No Second Stimulation Chosen\n")
	if Is_Second_Stim == 1:
		all_paramaters_combined_out.write("Is_Second_Stim = %f\n" % (Is_Second_Stim))
		all_paramaters_combined_out.write("Stim_per_frame2 = %f\n" % (Stim_per_frame2))
		all_paramaters_combined_out.write("P_site2 = %f\n" % (P_site2))
		all_paramaters_combined_out.write("P_site_start2 = %f\n" % (P_site_start2))
		all_paramaters_combined_out.write("P_decay2 = %f\n" % (P_decay2))
	
		all_paramaters_combined_out.write("T_end_start2 = %f\n" % (T_end_start2))
		all_paramaters_combined_out.write("T_endocytosis2 = %f\n" % (T_endocytosis2))
	

		all_paramaters_combined_out.write("Stim_start2 = %f\n" % (Stim_end2))
		all_paramaters_combined_out.write("Stim_end2 = %f\n" % (Stim_end2))


	all_paramaters_combined_out.close();

#--------------------#
#-----------------------------------------------#

#-----------------------------------------------#
# Level 3 is to aggregate the synapse release data into a single number
	t_tmp = np.zeros([Bundle_size,1])
	for x in range(0, Bundle_size):
	#	t_tmp[int(x)] = x
#		aggregate_synapse_ves_out.write("%f\t" % (float(x*0.1)))
#		aggregate_synapse_release_out.write("%f\t" % (float(x*0.1)))
		all_data_combined_out.write("%f\t" %(float(x*0.1)))
		for y in range(1, N_syns):
#			aggregate_synapse_out.write("%f\t" % (aggregate_bundle_static[int(y)][int(x)]) )
#			aggregate_synapse_ves_out.write("%f\t" % (aggregate_bundle_PoolSize_static[int(y)][int(x)]) )
#			aggregate_synapse_release_out.write("%f\t" % (aggregate_bundle_release_static[int(y)][int(x)]) )
			if y == 1:
				all_data_combined_out.write("%f\t%f\t%f\t" %(Intensity_mean[int(x)], ReleaseNumber_mean[int(x)],PoolSize_mean[int(x)]))
		
		
#		aggregate_synapse_out.write("\n" )
#		aggregate_synapse_ves_out.write("\n" )
#		aggregate_synapse_release_out.write("\n" )
		all_data_combined_out.write("\n")
	
#	aggregate_synapse_out.close()
#	aggregate_synapse_ves_out.close()
#	aggregate_synapse_release_out.close()
	all_data_combined_out.close()



	return ()

####################################################
