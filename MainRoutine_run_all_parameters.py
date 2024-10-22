#-------------------------------------------------------------------------#
# This is the main routine to generate simulated intensity profiles for a #
# sustained stimulation experiment                                        #
#-------------------------------------------------------------------------#


from generate_simulated_pHluorin_intensity_database import generate_sub_model 



# This is the hardcoded section of parameters

N_syns = 100                        # Define number of simulations to run for each parameter condition
Intensity_per_vesicle = 500         # Define the intensity per vesicle release event
P_site = 0.01                       # Define the release probability per release site per stimulus
P_max = 2.0                         # Define the initial multi-vesicular release (MVR) probability as a fraction the the native release probability
P_decay_start = 2                   # Define the number of stimulus pulses when the MVR begins to decay
P_decay = 20                        # Define the decay rate for the MVR
Stim_per_frame = 4                  # Define the number of stimulation pulses per frame (time-step)


# This is the main routine for the  simulated intesnity database
# This routine will output all simulated data in a folder called "Synapse Data"
# The sub-folder name will list the parameters of the simulation

for N_release_sites in range(1,22):
    for Stim_start in range(160, 200,5):
        for Stim_end in range((Stim_start+5), 200,5):
            for T_end_start in range(150,250,25):
                generate_sub_model(N_syns, Intensity_per_vesicle, N_release_sites, Stim_start, Stim_end, P_site, P_max,P_decay_start, P_decay,T_end_start, Stim_per_frame)