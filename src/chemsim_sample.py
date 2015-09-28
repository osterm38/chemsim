import simpy
import random

class Sample(object):
	def __init__(self,env,y,e,eId,ssId,s,sId,startTime,volume):
		self.env = env
		self.y = y
		self.e = e
		self.eId = eId
		self.ssId = ssId
		self.s = s
		self.sId = sId 
		self.startTime = startTime
		self.volume = volume

	def __str__(self):
		print "<y={y},e={e},eId={eId},ssId={ssId},s={s},sId={sId},startTime={startTime},volume={volume}>".format(
				y=self.y,
				e=self.e,
				eId=self.eId,
				ssId=self.ssId,
				s=self.s,
				sId=self.sId,
				startTime=self.startTime,
				volume=self.volume)

	def process(self):
		print "Begin processing sample {s} at time {t}.".format(s=self,t=self.env.now)
		assert env.self.now == 0, "Now should be 0, but instead is {0}".format(self.env.now)
		self.env.process(self.collect())
		self.env.process(self.transport())
		print "End processing sample {s} at time {t}.".format(s=self,t=self.env.now)

	def collect(self):
		print "Begin collecting sample {s} at time {t}".format(s=self,t=self.env.now)
		assert env.self.now == 0, "Now should be 0, but instead is {0}".format(self.env.now)
		yield env.process(simpy.timeout(self.startTime))
		print "End collecting sample {s} at time {t}".format(s=self,t=self.env.now)

	def transport(self,lab):
		print "Begin transporting sample {s} at time {t} to lab {l}".format(s=self,t=self.env.now,l=lab)
		assert env.self.now == self.startTime, "Now should be 0, but instead is {0}".format(self.env.now)
		with lab.transportResource().request() as transportReq:
			yield transportReq
		print "End transporting sample {s} at time {t} to lab {l}".format(s=self,t=self.env.now,l=lab)
