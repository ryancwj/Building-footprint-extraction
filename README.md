# Building-footprint-extraction
Script to extract building footprint from Microsoft's GlobalMLBuildingFootprints dataset

Use Read-files.py script to split raw .geojsonl to smaller readable .geojsonl files.
Use Extraction to extract data within polygon shapefile.
WARNING: Runtimes vary from 15 minutes to 4 hours depending on PC specs.

Malaysian building footprints have been processed and saved into shapefiles by respective states:
\\MYKUL1-STOR\Library\Water Resources\GIS Data\Building_Footprint\Data

Datasets of other countries are also available.
The dataset is faily accurate, up to 80% of the time. But due to the nature of AI/ML models, errors can occur.
For more information, please visit:
https://github.com/microsoft/GlobalMLBuildingFootprints

Extraction.py

Input requirements:
1. Shapefile (.shp)
2. Have one field name called "ID" with name of area (basin, administrative region, forest reserve etc.)
3. Do not use special characters in "ID" column (i.e. ?/>,*;:".)
4. Coordinate system as WGS84 (EPSG:4326)
5. Delete shapefile and dependencies from folder after use. Only one shapefile will run in the script.
   If multiple shapefile is in folder, script will only use the first shapefile it finds.

Output requirements:
1. Copy output building footprints out to another folder directory.
2. Delete any outputs in this folder.
3. Rerunning the script will overwrite the files if input shapefile shares the same ID.

Package requirements: os, pandas, geopandas. shapely
