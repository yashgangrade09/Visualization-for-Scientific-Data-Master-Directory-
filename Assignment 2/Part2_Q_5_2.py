from paraview.simple import *
arrow_list = []
shrink_list = []
extract_edge_list = []

for i in range(16):
	arrow = Arrow()
	arrow.TipResolution = 12
	arrow_list.append(arrow)

rv = GetActiveViewOrCreate('RenderView')

for i in range(16):
	shrink_list1 = Shrink(Input = arrow_list[i])
	shrink_list.append(shrink_list1)
	shrink1Display = Show(shrink_list[i], rv)
	shrink1Display.Orientation = [0,0,i*22.5]
	extract_edge_list1 = ExtractEdges(Input = arrow_list[i])
	extract_edge_list.append(extract_edge_list1)
	extractEdges1Display = Show(extract_edge_list[i], rv)
	extractEdges1Display.Orientation = [0,0,i*22.5]
	Render()