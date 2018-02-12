from paraview.simple import *
arrow_list = []

for i in range(16):
	arrow = Arrow()
	arrow.TipResolution = 12
	arrow_list.append(arrow)

rv = 