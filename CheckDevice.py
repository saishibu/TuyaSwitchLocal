import tinytuya

d=tinytuya.OutletDevice("8062300084cca891796a", "192.168.1.113", "35f21f39b189da3d36d665a8d5113c5d")
d.set_version(3.3)

data = d.status()
print(data)
