import arcpy

arcpy.env.workspace = "C:/GIS/HW07"

# Composite raster
arcpy.management.CompositeBands(
    ["red.tif", "green.tif", "blue.tif"],
    "landsat_composite.tif"
)

# Hillshade
arcpy.ddd.HillShade(
    "dem_30m.tif",
    "hillshade.tif",
    315,
    45
)

# Slope
arcpy.ddd.Slope(
    "dem_30m.tif",
    "slope.tif",
    "DEGREE"
)