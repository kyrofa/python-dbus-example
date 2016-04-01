#!/usr/bin/env python3

def invert(someBytes):
	return bytes(255 - byte for byte in someBytes)

