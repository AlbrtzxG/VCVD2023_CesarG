#EXAMPLEEEEEE TO USEEEEE 
#FOR USE THIS PROGRAM USE THE NEXT LINE 
# Python p2300709002.py --mass 1000 --V0 20 --uFac 0.65
__doc__ = " main methode"
#Import the library
import argparse
import sys

#Import the fuctions
from CODE.BrakesVelocity import Velocity_Time
from CODE.BrakesDistance import Distance_Time


def main_method():
  #ARG PARSE CONFIGURATION
  main_method.__doc__ = "sample main method"
  DataParse = argparse.ArgumentParser(description='Data for classes')
  DataParse.add_argument('--V0', type=float, help='Velocity KM/H')
  DataParse.add_argument('--mass', type=float, help='Mass in kg')
  DataParse.add_argument('--uFac', type=float, help='Coeficient of friction')

  # Analizar los argumentos de la línea de comandos
  Datargs = DataParse.parse_args()

  #Case for decide the name in case of RUN FROM VISUAL CODE 
  #IF FOR THE INITIAL VELOCITY
  if Datargs.V0 != None:
    print("The velocity is: ",Datargs.V0)
  else:
    Datargs.V0 = float(input("Wich Velocity does the car have? ")) / 3.6
  #IF FOR THE MASS
  if Datargs.mass != None:
    print("The mass is: ", Datargs.mass)
  else:
    Datargs.mass = float(input("What is the mass?"))
  #IF FOR THE FRICTION
  if Datargs.uFac != None:
    print("The friction Coeficient: ", Datargs.uFac)
  else:
    Datargs.uFac = float(input("Give me the friction? ")) / 3.6

  #Insert the values for the functions

  Velocity_Time(Datargs.V0, Datargs.mass, Datargs.uFac)
  Distance_Time(Datargs.V0, Datargs.mass, Datargs.uFac)

# Hacer el trabajo y llamar a un método.
main_method()

# Terminar el programa
sys.exit()
