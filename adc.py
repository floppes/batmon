#!/usr/bin/python

from abc import ABCMeta, abstractmethod

class ADC:
	def __init__(self, miso, mosi, clk, cs):
		self._miso = miso
		self._mosi = mosi
		self._clk = clk
		self._cs = cs
		
	@abstractmethod
	def get_resolution(self):
		pass
		
	@abstractmethod
	def setup_pins(self):
		pass
		
	@abstractmethod
	def read_value(self):
		pass