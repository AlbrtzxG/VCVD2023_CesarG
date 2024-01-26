#IMPORT THE EXTENSION
import matplotlib.pyplot as plt
import numpy as np
## ////////////////////////////////
''''
#Variables by the user
V0 = int(input("Wich Velocity have the car? ")) / 3.6
mass = int( input("Wich is the mass? "))
uFac = float(input("Give me the friction? "))
'''

#Maths and calculation
def Velocity_Time (Velocity_Time_doc, V0, mass, uFac):
    #Define variables
    Fr= uFac * 9.81 * mass 
    aceleration= Fr / mass
    time = V0 / aceleration

    fig = plt.figure()

    Velocity = fig.add_subplot(111)

    #data
    VelTime = V0 * aceleration
    t = np.arange(0.0 , time, 0.1)
    Vel = [V0 - aceleration * timer for timer in t]
    #print(Vel)
    #Define Plots
    Velocity.set_xlabel("Seconds")
    Velocity.set_ylabel("Velocity m/s")
    Velocity.plot(t, Vel, color="Green", lw=2)
    #print(t)
    fig.suptitle("Velocity Time of braking", fontweight="bold")

    plt.savefig(Velocity_Time_doc)

#nombre_archivo_pdf = "VelocityTime.pdf"

# Llamar a la función y exportar la gráfica como PDF
#Velocity_Time(nombre_archivo_pdf)





#print(V0)
