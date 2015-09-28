import simpy
import pandas as pd
import itertools as it
import random

from chemsim_sample import Sample
from chemsim_lab import Lab


class Enterprise(object):
	def __init__(self):
		self.env = simpy.Environment()


	def setup(self, eventsPerYearFile, samplesetsPerEventFile, samplesPerEventFile, sampleVolumeFile):
		"""create samples based off input files"""

		#Lab info
		self.Lab222S = Lab(env=self.env,transportResCap=2)
		self.LabRPL = Lab(env=self.env,transportResCap=2)
		
		
		#Dataframes for sample creation
		self.ePyDf  = pd.read_csv(eventsPerYearFile, index="Year")
		self.events = self.ePyDf.columns
		self.years  = self.ePyDf.index

		self.ssPeDf = pd.read_csv(samplesetsPerEventFile, index="Event", squeeze=True)
		assert self.ssPeDf.columns = self.events

		self.sPeDf = pd.read_csv(samplesPerEventFile, index="Sample")
		self.samples = self.sPeDf
		assert self.sPeDf.columns = self.events

		self.sVolDf = pd.read_csv(sampleVolumeFile, index="Sample", squeeze=True)
		
		#Create/start processing individual samples
		for y, e in it.product(self.years, self.events):
			numEvents = self.ePyDf.loc[y,e]
			for eId in xrange(numEvents):
				startTime = float(y) + random.uniform(0,365)
				numSets = self.ssPeDf[e]
				for ssId, s in it.product(xrange(numSets), self.samples):
					numSamples = self.sPeDf.loc[s,e]
					volume = self.sVolDf[s]
					for sId in xrange(numSamples):
						sample = Sample(env=env,
								y=y,
								e=e,
								eId=eId,
								ssId=ssId,
								s=s,
								sId=sId,
								startTime=startTime,
								volume=volume)
						self.env.process(sample.process())
						self.sampleList.append(sample)
