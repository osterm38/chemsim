import simpy

class Lab(object):
	def __init__(self,env,transportResCap):
		self.env = env
		self.transportResource = simpy.Resource(env,capacity=transportResCap)
