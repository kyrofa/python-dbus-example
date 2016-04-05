#!/usr/bin/env python3

def invert(someBytes):
	return bytes(255 - byte for byte in someBytes)

def explode(someBytes):
	result = bytes()
	for byte, count in zip(someBytes[0:], someBytes[1:]):
		result += bytes([byte]) * (1 << count)
	return result

