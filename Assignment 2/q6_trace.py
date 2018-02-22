#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
a2dvti = GetActiveSource()

# set active source
SetActiveSource(a2dvti)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2438, 1542]

# get color transfer function/color map for 'Scalars_'
scalars_LUT = GetColorTransferFunction('Scalars_')

# get opacity transfer function/opacity map for 'Scalars_'
scalars_PWF = GetOpacityTransferFunction('Scalars_')

# show data in view
a2dvtiDisplay = Show(a2dvti, renderView1)
# trace defaults for the display properties.
a2dvtiDisplay.Representation = 'Slice'
a2dvtiDisplay.ColorArrayName = ['POINTS', 'Scalars_']
a2dvtiDisplay.LookupTable = scalars_LUT
a2dvtiDisplay.OSPRayScaleArray = 'Scalars_'
a2dvtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a2dvtiDisplay.SelectOrientationVectors = 'None'
a2dvtiDisplay.ScaleFactor = 409.6
a2dvtiDisplay.SelectScaleArray = 'Scalars_'
a2dvtiDisplay.GlyphType = 'Arrow'
a2dvtiDisplay.GlyphTableIndexArray = 'Scalars_'
a2dvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
a2dvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
a2dvtiDisplay.ScalarOpacityUnitDistance = 22.538152910782735
a2dvtiDisplay.ScalarOpacityFunction = scalars_PWF

# show color bar/color legend
a2dvtiDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# hide data in view
Hide(a2dvti, renderView1)

# show data in view
a2dvtiDisplay = Show(a2dvti, renderView1)

# show color bar/color legend
a2dvtiDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitVertical(0, 0.5)

# set active view
SetActiveView(None)

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitHorizontal(1, 0.5)

# set active view
SetActiveView(None)

# set active view
SetActiveView(renderView1)

# show data in view
a2dvtiDisplay = Show(a2dvti, renderView1)

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2048.0, 1024.0, 10000.0]
renderView1.CameraFocalPoint = [2048.0, 1024.0, 0.0]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]

# show color bar/color legend
a2dvtiDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=a2dvti,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point2 = [4096.0, 2048.0, 0.0]

# set active view
SetActiveView(None)

# set active source
SetActiveSource(plotOverLine1)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [1214, 754]
lineChartView1.LeftAxisRangeMaximum = 6.66
lineChartView1.BottomAxisRangeMaximum = 6.66
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.TopAxisRangeMaximum = 6.66

# place view in the layout
layout1.AssignView(4, lineChartView1)

# show data in view
plotOverLine1Display = Show(plotOverLine1, lineChartView1)
# trace defaults for the display properties.
plotOverLine1Display.CompositeDataSetIndex = [0]
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'arc_length'
plotOverLine1Display.SeriesVisibility = ['Scalars_']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'Scalars_', 'Scalars_', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'Scalars_', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine1Display.SeriesPlotCorner = ['arc_length', '0', 'Scalars_', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesLabelPrefix = ''
plotOverLine1Display.SeriesLineStyle = ['arc_length', '1', 'Scalars_', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display.SeriesLineThickness = ['arc_length', '2', 'Scalars_', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display.SeriesMarkerStyle = ['arc_length', '0', 'Scalars_', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(None)

# set active source
SetActiveSource(plotOverLine1)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(None)

# set active source
SetActiveSource(a2dvti)

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=a2dvti)
warpByScalar1.Scalars = ['POINTS', 'Scalars_']

# set active source
SetActiveSource(warpByScalar1)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [2438, 753]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 0
renderView2.Background = [0.32, 0.34, 0.43]

# place view in the layout
layout1.AssignView(2, renderView2)

# show data in view
warpByScalar1Display = Show(warpByScalar1, renderView2)
# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.ColorArrayName = ['POINTS', 'Scalars_']
warpByScalar1Display.LookupTable = scalars_LUT
warpByScalar1Display.OSPRayScaleArray = 'Scalars_'
warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByScalar1Display.SelectOrientationVectors = 'None'
warpByScalar1Display.ScaleFactor = 409.6
warpByScalar1Display.SelectScaleArray = 'Scalars_'
warpByScalar1Display.GlyphType = 'Arrow'
warpByScalar1Display.GlyphTableIndexArray = 'Scalars_'
warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
warpByScalar1Display.ScalarOpacityFunction = scalars_PWF
warpByScalar1Display.ScalarOpacityUnitDistance = 22.554415895469933

# reset view to fit data
renderView2.ResetCamera()

# Properties modified on warpByScalar1
warpByScalar1.ScaleFactor = 1.25

# show data in view
warpByScalar1Display = Show(warpByScalar1, renderView2)

# reset view to fit data
renderView2.ResetCamera()

# show color bar/color legend
warpByScalar1Display.SetScalarBarVisibility(renderView2, True)

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, renderView2)
# trace defaults for the display properties.
plotOverLine1Display_1.Representation = 'Surface'
plotOverLine1Display_1.ColorArrayName = ['POINTS', 'Scalars_']
plotOverLine1Display_1.LookupTable = scalars_LUT
plotOverLine1Display_1.OSPRayScaleArray = 'Scalars_'
plotOverLine1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display_1.SelectOrientationVectors = 'None'
plotOverLine1Display_1.ScaleFactor = 409.6
plotOverLine1Display_1.SelectScaleArray = 'Scalars_'
plotOverLine1Display_1.GlyphType = 'Arrow'
plotOverLine1Display_1.GlyphTableIndexArray = 'Scalars_'
plotOverLine1Display_1.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display_1.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display_1.GaussianRadius = 204.8
plotOverLine1Display_1.SetScaleArray = ['POINTS', 'Scalars_']
plotOverLine1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display_1.OpacityArray = ['POINTS', 'Scalars_']
plotOverLine1Display_1.OpacityTransferFunction = 'PiecewiseFunction'

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.ViewSize = [1214, 753]
lineChartView2.LeftAxisRangeMaximum = 6.66
lineChartView2.BottomAxisRangeMaximum = 6.66
lineChartView2.RightAxisRangeMaximum = 6.66
lineChartView2.TopAxisRangeMaximum = 6.66

# place view in the layout
layout1.AssignView(6, lineChartView2)

# show data in view
plotOverLine1Display_2 = Show(plotOverLine1, lineChartView2)
# trace defaults for the display properties.
plotOverLine1Display_2.CompositeDataSetIndex = [0]
plotOverLine1Display_2.UseIndexForXAxis = 0
plotOverLine1Display_2.XArrayName = 'arc_length'
plotOverLine1Display_2.SeriesVisibility = ['Scalars_']
plotOverLine1Display_2.SeriesLabel = ['arc_length', 'arc_length', 'Scalars_', 'Scalars_', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_2.SeriesColor = ['arc_length', '0', '0', '0', 'Scalars_', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine1Display_2.SeriesPlotCorner = ['arc_length', '0', 'Scalars_', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_2.SeriesLabelPrefix = ''
plotOverLine1Display_2.SeriesLineStyle = ['arc_length', '1', 'Scalars_', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_2.SeriesLineThickness = ['arc_length', '2', 'Scalars_', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_2.SeriesMarkerStyle = ['arc_length', '0', 'Scalars_', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
lineChartView2.Update()

# destroy lineChartView2
Delete(lineChartView2)
del lineChartView2

# close an empty frame
layout1.Collapse(6)

# set active view
SetActiveView(renderView2)

#### saving camera placements for all active views

# current camera placement for renderView2
renderView2.CameraPosition = [1771.468816200583, -2944.810738537055, 3151.283043709927]
renderView2.CameraFocalPoint = [2047.9999999999998, 1023.9999999999999, 123.37499999999982]
renderView2.CameraViewUp = [-0.03758636618596178, 0.607782135115218, 0.7932138055478622]
renderView2.CameraParallelScale = 2291.3858252158234

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2048.0, 1024.0, 10000.0]
renderView1.CameraFocalPoint = [2048.0, 1024.0, 0.0]
renderView1.CameraParallelScale = 2289.7336089597848

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).