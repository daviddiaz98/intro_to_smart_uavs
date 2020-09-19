from calendar import timegm
from time import gmtime

class Drone:

	"""Drone class"""
	def _init_(self,fuel,max_spedd):
		""" Initializing Drone object"""
		self._fuel= fuel
		self._max_speed= max_speed
		self_speed= 0.
	def add_fuel(self,fuel):
		""" Adding fuel to tank"""
		sefl._fuel+=fuel
	def get_fuel(self):
		"""Getting Drone fuel"""
		return self._fuel
	def set_speed(sel,speed):
		"""Setting Drone speed"""
		self._speed = speed if speed < self._max_speed else self._max_speed
	def get_speed(self):
		""" Getting Drone speed"""
		return self._speed
	def fly(self):
		""" FLiying the drone"""
		print("fly")
		return

