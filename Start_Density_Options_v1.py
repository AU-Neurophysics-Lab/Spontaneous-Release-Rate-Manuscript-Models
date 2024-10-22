# -*- coding: utf-8 -*-
"""

This routine places the initial vesicle locations and speeds within the presynapse

"""

import numpy as np	#import package numpy and give it the designation "np"

def sub_startpoints_SV_v2D_1(Vel_high2D_x, Vel_high2D_y,P_size_oneD, presynapse_bundle_static2D, N_vesicles, startx, starty, start2D):

    # Start point of vesicles
# Generate random start points for each SV in the pool
    tmplst = [[float(0.0),float(0.0)] for x in range(int((P_size_oneD-2)*(P_size_oneD-2)))]
    for i in range(0, P_size_oneD-2):
        for j in range(0, P_size_oneD-2):
            tmplst[int(i*(P_size_oneD-2)+j)] = [i,j]

# Remove all x=0 options from list
    for i in range(0, P_size_oneD-2):
#        print(i,tmplst[int(i)])
        tmplst.remove(tmplst[int(0)])




    


# This section establishes the reserve pool vesicles

    res_frac = N_vesicles - round(N_vesicles*(0.18+0.85*np.exp(-N_vesicles/30)))
    start_spot = [startx,starty]
    start2D.append(start_spot)
    for q in range(1, res_frac):
        count_add = 0
        for ii in range(startx, P_size_oneD):
            for jj in range(starty, P_size_oneD):
                count = 0
                if len(start2D) > 0:
                    for qq in range(0,len(start2D)):        # loop through all of the previously added vesicles and find the next spot that hasn't been taken
                        if start2D[qq] == [ii,jj] and count == 0:
                            count = 1
                    if count == 0 and count_add ==0:
                        start2D.append([ii,jj])
                        count_add = 1

                        for ll in range(0, len(tmplst)-1):
                            if tmplst[ll] == [ii,jj]:  # Loop through the list of spots available to the recycling pool and remove the one just taken by the reserve pool
                                tmplst.remove(tmplst[ll])


    for q in range(0, res_frac):
        Vel_high2D_x.append(0)
        Vel_high2D_y.append(0)

# This section establishes the recycling pool vesicles

# Remove all options beyond reserve pool from list
    for i in range(0, len(tmplst)):
        if i < len(tmplst):
            if tmplst[int(i)] > [startx,starty]:
                for ii in range(i, len(tmplst)):
                     tmplst.remove(tmplst[int(i)])

    for q in range(res_frac,N_vesicles):
        tmpspt = int(np.random.rand()*int(len(tmplst)))
        start2D.append(tmplst[tmpspt])
        tmplst.remove(tmplst[tmpspt])
    # Start velocities of vesicles


    for q in range(res_frac,N_vesicles):
        tmpspt = int(np.random.rand()+0.5)
        if tmpspt == 0:
            Vel_high2D_x.append(-1)
        else: 
            Vel_high2D_x.append(1)
        tmpspt = int(np.random.rand()+0.5)
        if tmpspt == 0:
            Vel_high2D_y.append(-1)
        else: 
            Vel_high2D_y.append(1)
#            
#    start2D = [[7,0],[6,3],[0,4],[8,8],[7,3],[1,1],[3,0],[3,8],[3,4],[2,4],[3,2],[8,4]]
#    Vel_high2D_x = [-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1]
#    Vel_high2D_y = [1,1,-1,1,1,1,-1,1,1,-1,-1,1]

#    start2D = [[2, 1],[6,7],[4,5],[5, 4],[5,2],[1,1],[5, 0],[1,7],[5,1],[1,2],[4,6],[6,2],[0,4],[2,6], [4,0]]
#    Vel_high2D_x = [-1,-1,-1,1,-1,1,1,1,1,1,1,-1,1,-1,1]
#    Vel_high2D_y = [0,-1,1,-1,1,1,0,-1,-1,1,-1,1,-1,-1,-1]


    return()



def sub_startpoints_SV_unconstrained_v2D_1(Vel_high2D_x, Vel_high2D_y,P_size_oneD, presynapse_bundle_static2D, N_vesicles, startx, starty, start2D, P_size_oneD_Y):

    # Start point of vesicles
# Generate random start points for each SV in the pool
    
    tmplst = [[float(0.0),float(0.0)] for x in range(int((P_size_oneD)*(P_size_oneD_Y)))]
    for i in range(0, P_size_oneD):
        for j in range(0, P_size_oneD_Y):
            tmplst[int(i*(P_size_oneD_Y)+j)] = [i,j]

# Remove all x=0 options from list
    for i in range(0, P_size_oneD_Y):
#        print(i,tmplst[int(i)])
        tmplst.remove(tmplst[int(0)])
# Remove all y=0 options from list
    for ii in range(0, P_size_oneD):
        for kk in range(0 , len(tmplst)-1):
            if tmplst[kk] == [ii, 0]:
                tmplst.remove(tmplst[kk])




    for q in range(0,N_vesicles):
        tmpspt = int(np.random.rand()*int(len(tmplst)))
        if tmpspt > 0:
            start2D.append(tmplst[tmpspt])
            tmplst.remove(tmplst[tmpspt])
        if tmpspt == 0:
            start2D.append(tmplst[tmpspt+1])
            tmplst.remove(tmplst[tmpspt+1])
    # Start velocities of vesicles


    for q in range(0,N_vesicles):
        tmpspt = int(np.random.rand()+0.5)
        if tmpspt == 0:
            Vel_high2D_x.append(-1)
        else: 
            Vel_high2D_x.append(1)
            
        tmpspt = int(np.random.rand()+0.5)
        if tmpspt == 0:
            Vel_high2D_y.append(-1)
        else: 
            Vel_high2D_y.append(1)



    return()


def sub_startpoints_SV_v2D_2(Vel_high2D_x, Vel_high2D_y,P_size_oneD, presynapse_bundle_static2D, N_vesicles, startx, starty, start2D, Barrier_y):

    # Start point of vesicles
# Generate random start points for each SV in the pool
    tmplst = [[float(0.0),float(0.0)] for x in range(int((P_size_oneD-1)*(P_size_oneD-1)))]
    for i in range(0, P_size_oneD-1):
        for j in range(0, P_size_oneD-1):
            tmplst[int(i*(P_size_oneD-1)+j)] = [i,j]

# Remove all x=0 options from list
    for i in range(0, P_size_oneD-1):
#        print(i,tmplst[int(i)])
        tmplst.remove(tmplst[int(0)])




    


# This section establishes the reserve pool vesicles

    res_frac = N_vesicles - round(N_vesicles*(0.18+0.85*np.exp(-N_vesicles/30)))
    start_spot = [startx,starty]
    start2D.append(start_spot)

# Sub section fills in the barrier at y = 10 lattice sites for at least 2 layers deep.

    if P_size_oneD > Barrier_y:
        tmp_sz = res_frac 
        for ii in range(0,startx):
            start2D.append([ii,Barrier_y])
      # Remove lattice sites greater than the range available to the now constrained recycling pool
            for ii in range(1, Barrier_y):
                for jj in range(Barrier_y, P_size_oneD):
                    for kk in range(0 , len(tmplst)-1):
                        if tmplst[kk] == [ii, jj]:
                            tmplst.remove(tmplst[kk])
    if P_size_oneD > (Barrier_y+1):
        tmp_sz = res_frac 
        for ii in range(0,(startx)):
            start2D.append([ii,Barrier_y+1])
      # Remove lattice sites greater than the range available to the now constrained recycling pool
            for ii in range(0, Barrier_y+1):
                for jj in range(Barrier_y, P_size_oneD):
                    for kk in range(0 , len(tmplst)-1):
                        if tmplst[kk] == [ii, jj]:
                            tmplst.remove(tmplst[kk])

    if P_size_oneD > (Barrier_y+2):
        tmp_sz = res_frac 
        for ii in range(0,(startx)):
            start2D.append([ii,Barrier_y+2])
      # Remove lattice sites greater than the range available to the now constrained recycling pool
            for ii in range(0, Barrier_y+2):
                for jj in range(Barrier_y, P_size_oneD):
                    for kk in range(0 , len(tmplst)-1):
                        if tmplst[kk] == [ii, jj]:
                            tmplst.remove(tmplst[kk])

    if P_size_oneD <= Barrier_y:
        tmp_sz = res_frac
        
    for q in range(startx, tmp_sz):
        count_add = 0
        for ii in range(startx, P_size_oneD):
            for jj in range(starty, P_size_oneD):
                count = 0
                if len(start2D) > 0:
                    for qq in range(0,len(start2D)):        # loop through all of the previously added vesicles and find the next spot that hasn't been taken
                        if start2D[qq] == [ii,jj] and count == 0:
                            count = 1
                    if count == 0 and count_add ==0:
                        start2D.append([ii,jj])
                        count_add = 1

                        for ll in range(0, len(tmplst)-1):
                            if tmplst[ll] == [ii,jj]:  # Loop through the list of spots available to the recycling pool and remove the one just taken by the reserve pool
                                tmplst.remove(tmplst[ll])

    for ii in range(10, P_size_oneD):
        for jj in range(10, P_size_oneD):
            for kk in range(0 , len(tmplst)-1):
                if tmplst[kk] == [ii, jj]:
                    tmplst.remove(tmplst[kk])


    for q in range(0, res_frac):
        Vel_high2D_x.append(0)
        Vel_high2D_y.append(0)



# Remove all options beyond reserve pool from list
    for i in range(0, len(tmplst)):
        if i < len(tmplst):
            if tmplst[int(i)] > [startx,starty]:
                for ii in range(i, len(tmplst)):
                     tmplst.remove(tmplst[int(i)])

# This section establishes the recycling pool vesicles
    for q in range(res_frac,N_vesicles):
        tmpspt = int(np.random.rand()*int(len(tmplst)))
        start2D.append(tmplst[tmpspt])
        tmplst.remove(tmplst[tmpspt])
    # Start velocities of vesicles


    for q in range(res_frac,N_vesicles):
        tmpspt = int(np.random.rand()+0.5)
        if tmpspt == 0:
            Vel_high2D_x.append(-1)
        else: 
            Vel_high2D_x.append(1)
        tmpspt = int(np.random.rand()+0.5)
        if tmpspt == 0:
            Vel_high2D_y.append(-1)
        else: 
            Vel_high2D_y.append(1)
#            
#    start2D = [[7,0],[6,3],[0,4],[8,8],[7,3],[1,1],[3,0],[3,8],[3,4],[2,4],[3,2],[8,4]]
#    Vel_high2D_x = [-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1]
#    Vel_high2D_y = [1,1,-1,1,1,1,-1,1,1,-1,-1,1]

#    start2D = [[2, 1],[6,7],[4,5],[5, 4],[5,2],[1,1],[5, 0],[1,7],[5,1],[1,2],[4,6],[6,2],[0,4],[2,6], [4,0]]
#    Vel_high2D_x = [-1,-1,-1,1,-1,1,1,1,1,1,1,-1,1,-1,1]
#    Vel_high2D_y = [0,-1,1,-1,1,1,0,-1,-1,1,-1,1,-1,-1,-1]


    return()


def sub_startpoints_SV_v2D_3(Vel_high2D_x, Vel_high2D_y,P_size_oneD, presynapse_bundle_static2D, N_vesicles, startx, starty, start2D, P_size_oneD_Y):


    # Start point of vesicles
# Generate random start points for each SV in the pool
    tmplst = [[float(0.0),float(0.0)] for x in range(int((P_size_oneD)*(P_size_oneD_Y)))]
    for i in range(0, P_size_oneD):
        for j in range(0, P_size_oneD_Y):
            tmplst[int(i*(P_size_oneD_Y)+j)] = [i,j]

# Remove all x=0 options from list
    for i in range(0, P_size_oneD_Y):
#        print(i,tmplst[int(i)])
        tmplst.remove(tmplst[int(0)])
# Remove all y=0 options from list
    for ii in range(0, startx):
        for kk in range(0 , len(tmplst)-1):
            if tmplst[kk] == [ii, 0]:
                tmplst.remove(tmplst[kk])



    


# This section establishes the reserve pool vesicles

    res_frac = N_vesicles - round(N_vesicles*(0.18+(0.85)*np.exp(-(N_vesicles-0)/30)))
    start_spot = [startx,starty]
    start2D.append(start_spot)
    for q in range(1, res_frac):
        count_add = 0
        for ii in range(startx, P_size_oneD):
            for jj in range(starty, P_size_oneD_Y):
                count = 0
                if len(start2D) > 0:
                    for qq in range(0,len(start2D)):        # loop through all of the previously added vesicles and find the next spot that hasn't been taken
                        if start2D[qq] == [ii,jj] and count == 0:
                            count = 1
                    if count == 0 and count_add ==0:
                        start2D.append([ii,jj])
                        count_add = 1

                        for ll in range(0, len(tmplst)-1):
                            if tmplst[ll] == [ii,jj]:  # Loop through the list of spots available to the recycling pool and remove the one just taken by the reserve pool
                                tmplst.remove(tmplst[ll])


    for q in range(0, res_frac):
        Vel_high2D_x.append(0)
        Vel_high2D_y.append(0)

# This section establishes the recycling pool vesicles

# Remove all options beyond reserve pool from list
    for i in range(0, len(tmplst)):
        if i < len(tmplst):
            if tmplst[int(i)] > [startx,starty]:
                for ii in range(i, len(tmplst)):
                     tmplst.remove(tmplst[int(i)])

    for q in range(res_frac,N_vesicles):
        tmpspt = int(np.random.rand()*int(len(tmplst)))
        start2D.append(tmplst[tmpspt])
        tmplst.remove(tmplst[tmpspt])
    # Start velocities of vesicles


    for q in range(res_frac,N_vesicles):
        tmpspt = int(np.random.rand()+0.5)
        if tmpspt == 0:
            Vel_high2D_x.append(-1)
        else: 
            Vel_high2D_x.append(1)
        tmpspt = int(np.random.rand()+0.5)
        if tmpspt == 0:
            Vel_high2D_y.append(-1)
        else: 
            Vel_high2D_y.append(1)
#            
#    start2D = [[7,0],[6,3],[0,4],[8,8],[7,3],[1,1],[3,0],[3,8],[3,4],[2,4],[3,2],[8,4]]
#    Vel_high2D_x = [-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1]
#    Vel_high2D_y = [1,1,-1,1,1,1,-1,1,1,-1,-1,1]

#    start2D = [[2, 1],[6,7],[4,5],[5, 4],[5,2],[1,1],[5, 0],[1,7],[5,1],[1,2],[4,6],[6,2],[0,4],[2,6], [4,0]]
#    Vel_high2D_x = [-1,-1,-1,1,-1,1,1,1,1,1,1,-1,1,-1,1]
#    Vel_high2D_y = [0,-1,1,-1,1,1,0,-1,-1,1,-1,1,-1,-1,-1]

    return()
