#!/usr/bin/env python3

import dbus
import sys

def main():
	bus = dbus.SystemBus()
	remote_object = bus.get_object("com.example.SampleService", "/SomeObject")
	iface = dbus.Interface(remote_object, "com.example.SampleInterface")
	argBytes = bytes(int(arg, 16) for arg in sys.argv[1:])
	inverted = iface.invert(argBytes)
	print(':'.join('{:02X}'.format(x) for x in inverted))

if __name__ == '__main__':
	main()
