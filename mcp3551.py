#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from adc import ADC

class MCP3551(ADC):
	def setup_pins(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		
		GPIO.setup(self._miso, GPIO.IN)
		GPIO.setup(self._clk, GPIO.OUT)
		GPIO.setup(self._cs, GPIO.OUT)

	def get_resolution(self):
		return 2097152.0
		
	def read_value(self):
		GPIO.output(self._cs, True)
		GPIO.output(self._clk, True)

		start = time.clock()

		# toggle CS until SDO/RDY is low
		while True:
			GPIO.output(self._cs, False)
			time.sleep(0.001)

			if (GPIO.input(self._miso) == False):
				break

			GPIO.output(self._cs, True)

			if (time.clock() - start > 2):
				print "MCP3551 error: timeout"
				return 0

		# read in two overflow bits and 22 ADC bits
		adcraw = 0

		for i in range(24):
			GPIO.output(self._clk, False)
			GPIO.output(self._clk, True)

			adcraw <<= 1
			
			if (GPIO.input(self._miso)):
				adcraw |= 0x1

		time.sleep(0.001)
		GPIO.output(self._cs, True)

		if (adcraw & 0x400000):
			print "MCP3551 error: overflow high"
			
		if (adcraw & 0x800000):
			print "MCP3551 error: overflow low"
		
		# remove overflow and sign bits
		adcout = adcraw & 0x1FFFFF
		
		# convert to negative number if necessary
		if (adcraw & 0x200000):
			adcout = (~adcout & 0x1FFFFF) * -1 + 1
		
		return adcout
