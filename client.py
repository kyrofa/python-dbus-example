#!/usr/bin/env python3

import dbus

def main():
	bus = dbus.SessionBus()

	remote_object = bus.get_object("com.example.SampleService", "/SomeObject")

	iface = dbus.Interface(remote_object, "com.example.SampleInterface")

	pong = iface.Ping("ping")

	print('Got response: {!r}'.format(str(pong)))

if __name__ == '__main__':
	main()
