#!/bin/python

import zerorpc
import os

class server_funcs (object):
	def __init__(self):
		if not os.path.exists("./tmp"):
			os.mkdir("./tmp")

	def create(self, filename):
		pardir="./"
		file_name=pardir+filename
		fo = open (file_name, "w+")
		fo.close()

	def write(self, filename, data):
		pardir="./"
		file_name=pardir+filename
		fo = open (file_name, "w+")
		fo.write(data)
		fo.close()

	def delete(self, filename):
		pardir="./"
		file_name=pardir+filename
		os.remove(file_name)

s = zerorpc.Server(server_funcs())
s.bind("tcp://0.0.0.0:4242")
s.run()

