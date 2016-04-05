#!/usr/bin/env python3

import dbus
import sys

def main():
	bus = dbus.SystemBus()
	remote_object = bus.get_object("com.example.SampleService", "/SomeObject")
	iface = dbus.Interface(remote_object, "com.example.SampleInterface")
	action = sys.argv[1]
	argBytes = bytes(int(arg, 16) for arg in sys.argv[2:])
	result = (iface.get_dbus_method(action))(argBytes)
	print(':'.join('{:02X}'.format(x) for x in result))

if __name__ == '__main__':
	main()
