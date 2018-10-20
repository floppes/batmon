#!/usr/bin/env python

import RPi.GPIO as GPIO
from adc import ADC

class MCP3001(ADC):
	def setup_pins(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)

		GPIO.setup(self._miso, GPIO.IN)
		GPIO.setup(self._clk, GPIO.OUT)
		GPIO.setup(self._cs, GPIO.OUT)

	def get_resolution(self):
		return 1024.0

	def read_value(self):
		GPIO.output(self._clk, False)
		GPIO.output(self._cs, False)

		# 3 dummy clocks to start sampling and read null bit
		for i in range(3):
			GPIO.output(self._clk, True)
			GPIO.output(self._clk, False)

		# clock out data, MSB first
		adcout = 0

		for i in range(10):
			GPIO.output(self._clk, True)

			adcout <<= 1

			if (GPIO.input(self._miso)):
				adcout |= 0x1

			GPIO.output(self._clk, False)

		GPIO.output(self._cs, True)

		return adcout
