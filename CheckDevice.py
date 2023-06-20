import tinytuya

tinytuya.set_debug(True)

c = tinytuya.Cloud()

devices = c.getdevices()
print("Device List: %r" % devices)
