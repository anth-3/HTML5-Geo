# Include the Python Shapefile Library
import shapefile as sf

# Name of the shapefile to create
filename = 'shapefiles/geolocation'

# Create a /point/ shapefile, and turn on autoBalance
sf_w = sf.Writer(sf.POINT)
sf_w.autoBalance = 1

# Add the points
sf_w.point(-90.185278, 38.624722, 212)
sf_w.point(-89.788221, 38.4233, 18)
sf_w.point(-90.123129, 37.992331, 25)

# Create attribute information
sf_w.field('Name', 'C', 20)
sf_w.field('Description', 'C', 80)
sf_w.field('Timestamp', 'D')
sf_w.field('Accuracy', 'N', 4, 0)
sf_w.field('AltitudeAccuracy', 'N', 4, 0)
sf_w.field('Heading', 'N', 9, 6)
sf_w.field('Speed', 'N', 7, 4)

# Add attribute information
sf_w.record('Point 000000', 'This is the first point collected.', '2011-04-06T23:24:12+06:00', 20, 100, None, 0)
sf_w.record('Point 000001', 'This is the second point collected.', '2011-04-07T00:15:37+06:00', 10, 10, 37, 15.6464)
sf_w.record('Point 000002', 'This is the third point collected.', '2011-04-07T11:49:03+06:00', 60, 80, 147, 31.2928)

# Save the file
sf_w.save(filename)

# Create a projection file
prj = open("%s.prj" % filename, 'w')
epsg = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137, 298.257223563]],PRIMEM["Greenwich",0],UNIT["degree", 0.0174532925199433]]'
prj.write(epsg)
prj.close()