#!/usr/bin/env python3

from gi.repository import GLib

import dbus
import dbus.service
import dbus.mainloop.glib
import byte_ops

class SomeObject(dbus.service.Object):
	@dbus.service.method("com.example.SampleInterface", in_signature='ay', out_signature='ay')
	def invert(self, payload):
		justBytes = bytes(0 + x for x in payload)
		flippedBytes = byte_ops.invert(justBytes)
		return self.bytes2ay(flippedBytes)

	@dbus.service.method("com.example.SampleInterface", in_signature='ay', out_signature='ay')
	def explode(self, payload):
		justBytes = bytes(0 + x for x in payload)
		explodedBytes = byte_ops.explode(justBytes)
		return self.bytes2ay(explodedBytes)

	def bytes2ay(self, someBytes):
		return [dbus.Byte(x) for x in someBytes]
		

if __name__ == '__main__':
	dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

	bus = dbus.SystemBus()
	name = dbus.service.BusName("com.example.SampleService", bus)
	object = SomeObject(bus, '/SomeObject')

	mainloop = GLib.MainLoop()
	mainloop.run()
