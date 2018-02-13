from paraview.simple import *
# get active source.
a2dvti = GetActiveSource()

# set active source
SetActiveSource(a2dvti)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
a2dvtiDisplay = Show(a2dvti, renderView1)

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