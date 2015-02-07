#!/bin/python

import zerorpc

class clint():
	def __init__(self):
		self.c=zerorpc.Client()
		self.c.connect("tcp://127.0.0.1:4242")


