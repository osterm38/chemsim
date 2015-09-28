import simpy
import random
from chemsim_enterprise import Enterprise

# 0. initialize
#  read in data and assign to parameters/variables
# 1. create samples
#  create individual samples based off matrices
#  start process from time 0
#  a. creation = timeout 0 to y+unif(0,365)
#  b. transport = request truck resource, takes time (which facility)
#  c. process = iteratively, request workstation/equip/personnel

def run_sim(enterprise, endTime):

	#Initialize
	beginRun = time.time()

	#Step through sim
	while enterprise.env.peek() < endTime:
		enterprise.env.step()

	endRun = time.time()-beginRun
	print "Simulation of {d} days ({y} years) completed in {s} seconds ({m} minutes)".format(
			d=endTime, y=(endTime/365), s=endRun, m=(endRun/60))


def main():

	#Initialize parameters
	seed     = 0
	numYears = 10

	ePyFile  = "numEventsPerYear.csv"
	ssPeFile = "numSetsPerEvent.csv"
	sPeFile  = "numSamplesPerEvent.csv"
	sVolFile = "sampleVolume.csv"

	#Create enterprise with lab(s)/transportation/samples/etc.
	random.seed(seed)
	ent = Enterprise()

	ent.setup(eventsPerYearFile=ePyFile, 
			samplesetsPerEventFile=ssPeFile,
			samplePerEventFile=sPeFile,
			sampleVolumeFile=sVolFile)

	#Run the simpy simulation
	run_sim(ent, numYears*365)

	return ent


if __name__ == "__main__":
	ent = main()