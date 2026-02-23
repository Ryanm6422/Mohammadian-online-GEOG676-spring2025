import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = "Lab05 Toolbox"
        self.alias = ""
        self.tools = [GarageTool]


class GarageTool(object):
    def __init__(self):
        self.label = "Garage Buffer Intersect"
        self.description = "Buffers garage points and intersects with buildings."
        self.canRunInBackground = False

    def getParameterInfo(self):

        param0 = arcpy.Parameter(
            displayName="Garage Points",
            name="garagePoints",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"
        )

        param1 = arcpy.Parameter(
            displayName="Buildings",
            name="buildings",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"
        )

        param2 = arcpy.Parameter(
            displayName="Buffer Distance",
            name="bufferDistance",
            datatype="GPLinearUnit",
            parameterType="Required",
            direction="Input"
        )

        param3 = arcpy.Parameter(
            displayName="Output Feature Class",
            name="outputFC",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output"
        )

        return [param0, param1, param2, param3]

    def isLicensed(self):
        return True

    def execute(self, parameters, messages):

        garage_points = parameters[0].valueAsText
        buildings = parameters[1].valueAsText
        buffer_distance = parameters[2].valueAsText
        output_fc = parameters[3].valueAsText

        garage_buffer = arcpy.Buffer_analysis(
            garage_points,
            "in_memory\\garage_buffer",
            buffer_distance
        )

        arcpy.Intersect_analysis(
            [garage_buffer, buildings],
            output_fc,
            "ALL"
        )

        return