from helpers import *

vc = volume_change(flow_rate, 0, 6, 0.01)
print("Change (0-6)", vc)

vc = volume_change(flow_rate, 6, 10, 0.01)
print("Change (6-10)", vc)
