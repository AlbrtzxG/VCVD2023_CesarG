#IMPORT THE EXTENSION
import matplotlib.pyplot as plt
import numpy as np
## ////////////////////////////////

#Maths and calculation
def Distance_Time (V0, mass, uFac):
    #Define variables
    Fr= uFac * 9.81 * mass 
    aceleration= Fr / mass
    time = V0 / aceleration
    Dist = 0
    Distot = []
    fig2 = plt.figure()

    Distance = fig2.add_subplot(111)
   
    #data
    t = np.arange(0.0 , time, 0.1)
    Vel = [V0 - aceleration * timer for timer in t]
    for vel in Vel:
        Dist += vel * 0.1 
        Distot.append(Dist)
    #Define Plots
    Distance.set_xlabel("Seconds")
    Distance.set_ylabel("Distance m")
    Distance.plot(t, Distot, color="Green", lw=2)
    
    fig2.suptitle("Distance Time of braking", fontweight="bold")
    #print(Distot)
    #print(t)
    plt.savefig("DistanceTime.pdf")

