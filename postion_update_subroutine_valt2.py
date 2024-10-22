# -*- coding: utf-8 -*-
"""


@author: mwg0016
"""


def sub_condition3_SV_v2D_1(t, q, con1_2D_x, con1_2D_y, Vel_high2D_x, Vel_high2D_y, presynapse_bundle_static2D, vesicle_time_bundle2D_x,vesicle_time_bundle2D_y, tmp_move_2D_x, tmp_move_2D_y, P_size_oneD,P_size_oneD_Y):


    # We need to do two things up front
    # (1) Save the velocity in a temporary variable before changing it in each conditional
    # (2) Create a variable to determine if all conditionals failed, and thus tell the vesicle to stay put this time-step
    tmp_vx = Vel_high2D_x[q]
    tmp_vy = Vel_high2D_y[q]
    con3 = 1
    
    # Condition 1a Flip y-velocity and check
    Vel_high2D_y[q] = -tmp_vy
    tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
    tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
    # Confirm that the new y-postion is not out of bounds
    if tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:

        if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 :
            vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
            vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
            con3 = 0

    # Condition 1b Flip x-velocity and check
    if con3 == 1:
        Vel_high2D_x[q] = -tmp_vx
        Vel_high2D_y[q] = tmp_vy
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
    
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con3 = 0


    # Condition 1c Flip y and x-velocities and check
    if con3 == 1:
        Vel_high2D_y[q] = -tmp_vy
        Vel_high2D_x[q] = -tmp_vx
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con3 = 0

    # Condition 1d set x-velocity to be zero and check
    if con3 == 1:
        Vel_high2D_x[q] = 0
        Vel_high2D_y[q] = tmp_vy
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
            vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
            vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
            con3 = 0

    # Condition 1e set x-velocity to be zero and flip y-velocity check
    if con3 == 1:
        Vel_high2D_x[q] = 0
        Vel_high2D_y[q] = -tmp_vy
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con3 = 0

    # Condition 1f set y-velocity to be zero and check
    if con3 == 1:
        Vel_high2D_y[q] = 0
        Vel_high2D_x[q] = tmp_vx
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
            vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
            vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
            con3 = 0

    # Condition 1g set y-velocity to be zero and flip x-velocity check
    if con3 == 1:
        Vel_high2D_y[q] = 0
        Vel_high2D_x[q] = -tmp_vx
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:

            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con3 = 0

    # Condition 1h set x-velocity to be zero and flip y-velocity check
    if con3 == 1:
        Vel_high2D_x[q] = 0
        Vel_high2D_y[q] = -tmp_vy
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )

        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:

            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con3 = 0

    # Condition 1i if all other lattice sites are occupied, then don't move this time-step
    if con3 == 1:
        vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1])
        vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1])
        Vel_high2D_x[q] = tmp_vx
        Vel_high2D_y[q] = tmp_vy

    return()

def sub_condition3_SV_v2D_2(t, q, con1_2D_x, con1_2D_y, Vel_high2D_x, Vel_high2D_y, presynapse_bundle_static2D, vesicle_time_bundle2D_x,vesicle_time_bundle2D_y, tmp_move_2D_x, tmp_move_2D_y, P_size_oneD,P_size_oneD_Y):


    # We need to do two things up front
    # (1) Save the velocity in a temporary variable before changing it in each conditional
    # (2) Create a variable to determine if all conditionals failed, and thus tell the vesicle to stay put this time-step
    tmp_vx = Vel_high2D_x[q]
    tmp_vy = Vel_high2D_y[q]
    con4 = 1
    
    # Condition 2a Flip x-velocity and check
    Vel_high2D_x[q] = -tmp_vx
    tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
    tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
    if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
        if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
            vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
            vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
            con4 = 0

    # Condition 2b Flip x-velocity and add y-velocity  check
    if con4 == 1:
        Vel_high2D_x[q] = -tmp_vx
        Vel_high2D_y[q] = tmp_vx
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con4 = 0


    # Condition 2c Flip x and add y-velocity flipped and check
    if con4 == 1:
        Vel_high2D_y[q] = -tmp_vx
        Vel_high2D_x[q] = -tmp_vx
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:

            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con4 = 0

    # Condition 2d set x-velocity to be zero and check
    if con4 == 1:
        Vel_high2D_x[q] = 0
        Vel_high2D_y[q] = tmp_vx
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con4 = 0

    # Condition 2e set x-velocity to be zero and flip y-velocity check
    if con4 == 1:
        Vel_high2D_x[q] = 0
        Vel_high2D_y[q] = -tmp_vx
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con4 = 0

    # Condition 2f keep x-velocity and add y-velocity and check
    if con4 == 1:
        Vel_high2D_y[q] = tmp_vx
        Vel_high2D_x[q] = tmp_vx
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con4 = 0

    # Condition 2g keep x-velocity and add y-velocity and flip and  check
    if con4 == 1:
        Vel_high2D_y[q] = -tmp_vx
        Vel_high2D_x[q] = tmp_vx
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con4 = 0

    # Condition 2h set x-velocity to be zero and flip y-velocity check
    if con4 == 1:
        Vel_high2D_x[q] = 0
        Vel_high2D_y[q] = -tmp_vx
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con4 = 0

    # Condition 2i if all other lattice sites are occupied, then don't move this time-step
    if con4 == 1:
        vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1])
        vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1])
        Vel_high2D_x[q] = tmp_vx
        Vel_high2D_y[q] = tmp_vy

    return()

def sub_condition3_SV_v2D_3(t, q, con1_2D_x, con1_2D_y, Vel_high2D_x, Vel_high2D_y, presynapse_bundle_static2D, vesicle_time_bundle2D_x,vesicle_time_bundle2D_y, tmp_move_2D_x, tmp_move_2D_y, P_size_oneD, P_size_oneD_Y):


    # We need to do two things up front
    # (1) Save the velocity in a temporary variable before changing it in each conditional
    # (2) Create a variable to determine if all conditionals failed, and thus tell the vesicle to stay put this time-step
    tmp_vx = Vel_high2D_x[q]
    tmp_vy = Vel_high2D_y[q]
    con5 = 1
    
    # Condition 3a Flip y-velocity and check
    Vel_high2D_y[q] = -tmp_vy
    tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
    tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
    if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0: 
        if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
            vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
            vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
            con5 = 0

    # Condition 3b Flip y-velocity and add x-velocity  check
    if con5 == 1:
        Vel_high2D_x[q] = -tmp_vy
        Vel_high2D_y[q] = tmp_vy
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0: 
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con5 = 0


    # Condition 3c Flip x and add y-velocity flipped and check
    if con5 == 1:
        Vel_high2D_y[q] = -tmp_vy
        Vel_high2D_x[q] = -tmp_vy
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0: 
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con5 = 0
    
    # Condition 3d set x-velocity to be zero and check
    if con5 == 1:
        Vel_high2D_x[q] = tmp_vy
        Vel_high2D_y[q] = 0
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con5 = 0

    # Condition 3e set x-velocity to be zero and flip y-velocity check
    if con5 == 1:
        Vel_high2D_x[q] = -tmp_vy
        Vel_high2D_y[q] = 0
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con5 = 0

    # Condition 3f keep x-velocity and add y-velocity and check
    if con5 == 1:
        Vel_high2D_y[q] = tmp_vy
        Vel_high2D_x[q] = tmp_vy
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con5 = 0

    # Condition 3g keep x-velocity and add y-velocity and flip and  check
    if con5 == 1:
        Vel_high2D_y[q] = -tmp_vy
        Vel_high2D_x[q] = tmp_vy
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con5 = 0

    # Condition 3h set x-velocity to be zero and flip y-velocity check
    if con5 == 1:
        Vel_high2D_x[q] = -tmp_vy
        Vel_high2D_y[q] = 0
        tmp_move_2D_y = (vesicle_time_bundle2D_y[int(q)][int(t-1)] + Vel_high2D_y[q] )
        tmp_move_2D_x = (vesicle_time_bundle2D_x[int(q)][int(t-1)] + Vel_high2D_x[q] )
        if tmp_move_2D_x < (P_size_oneD) and tmp_move_2D_x > 0 and tmp_move_2D_y < (P_size_oneD_Y) and tmp_move_2D_y > 0:
            if int(presynapse_bundle_static2D[int(tmp_move_2D_x)][int(tmp_move_2D_y)]) == 0 and tmp_move_2D_y != len(presynapse_bundle_static2D[1]) and tmp_move_2D_y != 0 and tmp_move_2D_x != len(presynapse_bundle_static2D[0]) and tmp_move_2D_x != 0:
                vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1] + Vel_high2D_x[q])
                vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1] + Vel_high2D_y[q])
                con5 = 0

    # Condition 3i if all other lattice sites are occupied, then don't move this time-step
    if con5 == 1:
        vesicle_time_bundle2D_x[int(q)][t] = (vesicle_time_bundle2D_x[int(q)][t-1])
        vesicle_time_bundle2D_y[int(q)][t] = (vesicle_time_bundle2D_y[int(q)][t-1])
        Vel_high2D_x[q] = tmp_vx
        Vel_high2D_y[q] = tmp_vy

    return()








def sub_update_SV_position_v1D_1():


    for q in range(0,(N_vesicles)):
    
        tmp_move = (vesicle_time_bundle[q][int(t-1)] + Vel_high[q] )
        con1 = 0
        con2 = 0
        
        # If next lattice site is an edge
        if tmp_move >= len(presynapse_bundle_static[0]) or tmp_move <= 0:
            if tmp_move <= 0:
                surface_hit_count.append([t, 1])
    
            con1 = 1
            Vel_high[q] = -Vel_high[q]
            tmp_move = (vesicle_time_bundle[q][int(t-1)] + Vel_high[q] )
    
            # If reverse lattice site is also occupied, don't move this time-step
            if (presynapse_bundle_static[0][int(tmp_move)]  >=  int(1) ) :
                vesicle_time_bundle[q][t] = (vesicle_time_bundle[q][int(t-1)])
                # Now find out which vesicle it hit and reverse that vesicles velocity
                ves_tmp = int(presynapse_bundle_static[0][int(tmp_move)])
                Vel_high[ves_tmp] = -Vel_high[ves_tmp]
    
    
        # If reverse lattice site is NOT occupied, move this time-step
            if ( presynapse_bundle_static[0][int(tmp_move)]  ==  int(0) ) :
                vesicle_time_bundle[q][t] = (vesicle_time_bundle[q][int(t-1)] + Vel_high[q])
                    
    
    
        # If next lattice site is NOT an edge
        if tmp_move < len(presynapse_bundle_static[0]) or tmp_move > 0 and con1 == 0:
    
        # If next lattice site is NOT an edge, If lattice site is NOT occupied, move this time-step
            if (presynapse_bundle_static[0][int(tmp_move)]  ==  int(0) ) :
                vesicle_time_bundle[q][t] = (vesicle_time_bundle[q][int(t-1)] + Vel_high[q])
    
        # If next lattice site is NOT an edge, If lattice site is occupied, reverse 
            if (presynapse_bundle_static[0][int(tmp_move)]  >=  int(1)  and con1 == 0) :
                # Now find out which vesicle it hit and reverse that vesicles velocity
                ves_tmp = int(presynapse_bundle_static[0][int(tmp_move)])
                Vel_high[ves_tmp-1] = -Vel_high[ves_tmp-1]
                Vel_high[q] = -Vel_high[q]
                tmp_move = (vesicle_time_bundle[q][int(t-1)] + Vel_high[q] )
    
    
                
        # If next lattice site is NOT an edge, If lattice site is occupied, If reverse site is an edge then don't move this time-step
                if tmp_move >= len(presynapse_bundle_static[0]) or tmp_move <= 0:
                    vesicle_time_bundle[q][t] = (vesicle_time_bundle[q][int(t-1)])
                    con2 = 1
                    
                if con2 == 0:
        # If next lattice site is NOT an edge, If lattice site is occupied, If reverse site is NOT an edge, If site is occupied
                    if (presynapse_bundle_static[0][int(tmp_move)]  >=  int(1) ) :
                        vesicle_time_bundle[q][t] = (vesicle_time_bundle[q][int(t-1)])
                    
        # If next lattice site is NOT an edge, If lattice site is occupied, If reverse site is NOT an edge, If reverse site is NOT occupied
                    if (presynapse_bundle_static[0][int(tmp_move)]  ==  int(0) ) and con1 == 0:
                        vesicle_time_bundle[q][t] = (vesicle_time_bundle[q][int(t-1)] + Vel_high[q])
    

    return()