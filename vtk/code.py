import numpy
from vtk import *
from vtk.util import numpy_support as VN

#reader = vtkStructuredPointsReader()
#reader.setFileName(file)
file_name = "1.vtk"

reader = vtkUnstructuredGridReader()
reader.SetFileName(file_name)
reader.Update()
output = reader.GetOutput()
scalar_range = output.GetScalarRange()

mapper = vtkDataSetMapper()
mapper.SetInput(output)
mapper.SetScalarRange(scalar_range)

actor = vtkActor()
actor.SetMapper(mapper)

renderer = vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground (1, 1, 1)

renderer_window = vtkRenderWindow()
renderer_window.AddRenderer(renderer)

interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderer_window)
interactor.Initialize()
interactor.Start()