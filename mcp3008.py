#!/usr/bin/env python

import RPi.GPIO as GPIO
from adc import ADC

class MCP3008(ADC):
	def __init__(self, miso, mosi, clk, cs, channel):
		ADC.__init__(self, miso, mosi, clk, cs)
		self._channel = channel
	
	def setup_pins(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		
		GPIO.setup(self._miso, GPIO.IN)
		GPIO.setup(self._mosi, GPIO.OUT)
		GPIO.setup(self._clk, GPIO.OUT)
		GPIO.setup(self._cs, GPIO.OUT)
		
	def get_resolution(self):
		return 1024.0
		
	def read_value(self):
		if ((self._channel > 7) or (self._channel < 0)):
			return -1

		GPIO.output(self._cs, True)
		GPIO.output(self._clk, False)
		GPIO.output(self._cs, False)

		commandout = self._channel
		commandout |= 0x18  # start bit + single-ended bit
		commandout <<= 3    # we only need to send 5 bits here
	
		for i in range(5):
			if (commandout & 0x80):
				GPIO.output(self._mosi, True)
			else:
				GPIO.output(self._mosi, False)

			commandout <<= 1
			GPIO.output(self._clk, True)
			GPIO.output(self._clk, False)

		adcout = 0
		
		# read in one empty bit, one null bit and 10 ADC bits
		for i in range(12):
			GPIO.output(self._clk, True)
			GPIO.output(self._clk, False)
			adcout <<= 1
			
			if (GPIO.input(self._miso)):
				adcout |= 0x1

		GPIO.output(self._cs, True)

		adcout /= 2       # first bit is 'null' so drop it
		
		return adcout
