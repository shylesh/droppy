#!/bin/python

import os

import pyinotify
import client
#import WatchManager, Notifier,  ProcessEvent

wm = pyinotify.WatchManager()
conn = client.clint()

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE
create_list = []
delete_list = []
global create_counter
global delete_counter
create_counter = 0
delete_counter = 0

class PTmp(pyinotify.ProcessEvent):
	def process_IN_CREATE(self, event):
		global create_counter
	#	print "Create call: %s" % os.path.join (event.path, event.name)
		check_counter()
		create_list.append(os.path.join (event.path, event.name))
		create_counter = create_counter + 1


	def process_IN_DELETE(self, event):
		global delete_counter
	#	print "Delete call: %s" % os.path.join (event.path, event.name)
		check_counter()
		delete_list.append(os.path.join (event.path, event.name))
		delete_counter = delete_counter + 1



notifier = pyinotify.Notifier(wm, PTmp())

wdd = wm.add_watch ('/tmp', mask, rec=False)

def check_counter():
	global create_counter
	global delete_counter

	if create_counter == 10:
		print "****CREATE LIST ****"
		for ele in create_list:
			conn.c.create(ele)
		create_counter = 0

	if delete_counter == 10:
		print "*****DELTE LIST****"
		for ele in delete_list:
			conn.c.delete(ele)
		delete_counter = 0

	return


notifier.loop()

