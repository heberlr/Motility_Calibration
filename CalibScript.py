import numpy as np
import shlex,subprocess
from subprocess import DEVNULL, STDOUT, check_call
from LF_MCMC import ABC_MCMC
import sys, os

def ModelRed(Par):
  # argv[1] = ID_simulation, argv[2] = pers_time, argv[3] = bias, and argv[4] = speed
  run = "./PhysiCell_model/motility2D.exe 0 15.0 "+str(Par[0])+" "+str(Par[1])
  #print(run)
  args = shlex.split(run)
  p = subprocess.Popen(args,stdout=DEVNULL)
  if p.wait() != 0:
    sys.exit("There was an error")
  outputFile = "./output0000"
  output = np.loadtxt(outputFile, dtype='f', delimiter='\t')
  displacement = np.array(output[:,1])
  if os.path.exists(outputFile):
    os.remove(outputFile)
  else:
    sys.exit("The file does not exist")
  return displacement
  
def ModelGreen(Par):
  # argv[1] = ID_simulation, argv[2] = pers_time, argv[3] = bias, and argv[4] = speed
  run = "./PhysiCell_model/motility2D.exe 0 15.0 "+str(Par[0])+" "+str(Par[1])
  #print(run)
  args = shlex.split(run)
  p = subprocess.Popen(args,stdout=DEVNULL)
  if p.wait() != 0:
    sys.exit("There was an error")
  outputFile = "./output0000"
  output = np.loadtxt(outputFile, dtype='f', delimiter='\t')
  displacement = np.array(output[:,1])
  if os.path.exists(outputFile):
    os.remove(outputFile)
  else:
    sys.exit("The file does not exist")
  return displacement

#Data
Temp, DsRedDisplacement, DsRedDisplacementSTD, GFPDisplacement, GFPDisplacementSTD = [], [], [], [], []
for line in open('./ObsData.dat', 'r'):
  values = [float(s) for s in line.split()]
  Temp.append(values[0])
  DsRedDisplacement.append(values[1])
  DsRedDisplacementSTD.append(values[2])
  GFPDisplacement.append(values[3])
  GFPDisplacementSTD.append(values[4])
Temp = np.array(Temp)
DsRedDisplacement = np.array(DsRedDisplacement)
DsRedDisplacementSTD = np.array(DsRedDisplacementSTD)
GFPDisplacement = np.array(GFPDisplacement)
GFPDisplacementSTD = np.array(GFPDisplacementSTD)

# Prior distribution uniform
UpperLimit = np.array([0.5,0.5])
LowLimit = np.array([0.0,0.0])
qoiR = DsRedDisplacement
qoiG = GFPDisplacement

ABC_MCMC(ModelRed, qoiR,LowLimit, UpperLimit,'./output/CalibMotR.dat',15.0,1)
ABC_MCMC(ModelGreen, qoiG,LowLimit, UpperLimit,'./output/CalibMotG.dat',20.0,1)
