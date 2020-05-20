import vtk
import time

cone = vtk.vtkConeSource ()
cone.SetHeight( 10.0 )
cone.SetRadius( 5.0 )
cone.SetResolution( 10 )

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cone.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

filename = "wheel1.stl"
 
reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
 
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)


window = vtk.vtkRenderWindow() # Sets the pixel width, length of the window.
window.SetSize(500, 500)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

renderer = vtk.vtkRenderer()
window.AddRenderer(renderer)

renderer.AddActor(actor)
renderer.AddActor(actor1)
#renderer.SetBackground(1, 0.1, 0.4)
renderer.SetBackground(0, 0, 1)

actor.SetOrigin(1,0,0)
actor1.SetPosition(0,5,0)
actor1.SetOrigin(-4.5,9,10)


window.Render()
time.sleep(1)
for i in range(9):
    actor.RotateY(10)
    actor1.RotateY(10)
    window.Render()
    time.sleep(0.1)

for i in range(36):
    actor.RotateY(10)
    actor1.RotateX(10)
    window.Render()
    time.sleep(0.1)
    
for i in range(18):
    actor.RotateY(10)
    actor1.RotateZ(10)
    window.Render()
    time.sleep(0.1)

#iren.Start()
interactor.Start()