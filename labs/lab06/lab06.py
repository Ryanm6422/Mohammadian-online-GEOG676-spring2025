import arcpy
import time

input_layer = arcpy.GetParameterAsText(0)
field_name = arcpy.GetParameterAsText(1)

arcpy.SetProgressor("step", "Starting map generation...", 0, 4, 1)

arcpy.SetProgressorLabel("Accessing current project...")
aprx = arcpy.mp.ArcGISProject("CURRENT")
m = aprx.activeMap
arcpy.SetProgressorPosition()
time.sleep(0.5)

arcpy.SetProgressorLabel("Getting layer...")
layer = m.listLayers(input_layer)[0]
arcpy.SetProgressorPosition()
time.sleep(0.5)

arcpy.SetProgressorLabel("Applying graduated color renderer...")
sym = layer.symbology
sym.updateRenderer("GraduatedColorsRenderer")
sym.renderer.classificationField = field_name
sym.renderer.breakCount = 5
layer.symbology = sym
arcpy.SetProgressorPosition()
time.sleep(0.5)

arcpy.SetProgressorLabel("Map generation complete.")
arcpy.SetProgressorPosition()

arcpy.AddMessage("Graduated color map successfully created.")