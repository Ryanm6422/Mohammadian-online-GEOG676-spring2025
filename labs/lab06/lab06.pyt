import arcpy
import time

class Toolbox(object):
    def __init__(self):
        self.label = "Lab06"
        self.alias = "Lab06"
        self.tools = [MapGenerator]

class MapGenerator(object):
    def __init__(self):
        self.label = "Generate Graduated Color Map"
        self.description = "Applies graduated color symbology to a layer."
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []

        input_layer = arcpy.Parameter(
            displayName="Input Layer",
            name="input_layer",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        field_name = arcpy.Parameter(
            displayName="Field for Classification",
            name="field_name",
            datatype="Field",
            parameterType="Required",
            direction="Input")

        field_name.parameterDependencies = [input_layer.name]

        params.append(input_layer)
        params.append(field_name)

        return params

    def execute(self, parameters, messages):

        input_layer = parameters[0].valueAsText
        field_name = parameters[1].valueAsText

        arcpy.SetProgressor("step", "Starting map generation...", 0, 4, 1)

        arcpy.SetProgressorLabel("Accessing project...")
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        m = aprx.activeMap
        arcpy.SetProgressorPosition()
        time.sleep(0.5)

        arcpy.SetProgressorLabel("Getting layer...")
        layer = parameters[0].value
        arcpy.SetProgressorPosition()
        time.sleep(0.5)

        arcpy.SetProgressorLabel("Applying symbology...")
        sym = layer.symbology
        sym.updateRenderer("GraduatedColorsRenderer")
        sym.renderer.classificationField = field_name
        sym.renderer.breakCount = 5
        layer.symbology = sym
        arcpy.SetProgressorPosition()
        time.sleep(0.5)

        arcpy.SetProgressorLabel("Complete.")
        arcpy.SetProgressorPosition()

        arcpy.AddMessage("Graduated color map created successfully.")