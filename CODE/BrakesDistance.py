#IMPORT THE EXTENSION
import matplotlib.pyplot as plt
import numpy as np
## ////////////////////////////////
'''
#Variables by the user
V0 = int(input("Wich Velocity have the car? ")) / 3.6
mass = int( input("Wich is the mass? "))
uFac = float(input("Give me the friction? "))
'''

#Maths and calculation
def Distance_Time (Distance_Time_doc, V0, mass, uFac):
    #Define variables
    Fr= uFac * 9.81 * mass 
    aceleration= Fr / mass
    time = V0 / aceleration
    Dist = 0
    Distot = []
    fig2 = plt.figure()

    Distance = fig2.add_subplot(111)
   
    #data
    VelTime = V0 * aceleration
    t = np.arange(0.0 , time, 0.1)
    Vel = [V0 - aceleration * timer for timer in t]
    for vel in reversed(Vel):
        Dist += vel * 0.1 
        Distot.append(Dist)
    #Define Plots
    Distance.set_xlabel("Seconds")
    Distance.set_ylabel("Distance m")
    Distance.plot(t, Distot, color="Green", lw=2)
    
    fig2.suptitle("Distance Time of braking", fontweight="bold")
    #print(Distot)
    #print(t)
    plt.savefig(Distance_Time_doc)

#nombre_archivo_pdf = "DistanceTime.pdf"

# Llamar a la función y exportar la gráfica como PDF
#Distance_Time(nombre_archivo_pdf)
