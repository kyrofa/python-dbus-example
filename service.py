#!/usr/bin/env python3

from gi.repository import GLib

import dbus
import dbus.service
import dbus.mainloop.glib

class SomeObject(dbus.service.Object):
	@dbus.service.method("com.example.SampleInterface", in_signature='s',
	                     out_signature='s')
	def Ping(self, message):
		return self.pong(message)

	def pong(self, message):
		return 'Pong-- got {!r}'.format(str(message))

if __name__ == '__main__':
	dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

	session_bus = dbus.SessionBus()
	name = dbus.service.BusName("com.example.SampleService", session_bus)
	object = SomeObject(session_bus, '/SomeObject')

	mainloop = GLib.MainLoop()
	mainloop.run()
