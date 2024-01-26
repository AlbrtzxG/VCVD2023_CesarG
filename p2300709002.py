__doc__ = " main methode"
#Import the library
import argparse
import sys

#Import the fuctions
from CODE.BrakesVelocity import Velocity_Time
from CODE.BrakesDistance import Distance_Time

# ArgParse Configuration
velparser = argparse.ArgumentParser(description='Proces for graphic velocity')
velparser.add_argument('--Velocity_PDF', type=str, help='file name for graph')

distparser = argparse.ArgumentParser(description='Proces for graphic velocity')
distparser.add_argument('--Dist_PDF', type=str, help='file name for graph')

# Analizar los argumentos de la línea de comandos
Velargs = velparser.parse_args()
Distargs = distparser.parse_args()
#Case for decide the name 

if Velargs.Velocity_PDF != None:
  print (Velargs.Velocity_PDF)
else:
  Velargs.Velocity_PDF = "Velocity.pdf"

if Distargs.Dist_PDF != None:
  print (Distargs.Dist_PDF)
else:
  Distargs.Dist_PDF = "Distance.pdf"

# Un método
def main_method():
  main_method.__doc__ = "sample main method"

  #Insert the values for the functions
  V0 = int(input("Wich Velocity does the car have? ")) / 3.6
  mass = int(input("What is the mass? "))
  uFac = float(input("Give me the friction? "))

  Velocity_Time(Velargs.Velocity_PDF,V0, mass, uFac)
  Distance_Time(Distargs.Dist_PDF,V0, mass, uFac)

# Hacer el trabajo y llamar a un método
main_method()

# Terminar el programa
sys.exit()
