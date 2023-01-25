import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
from geopandas import GeoDataFrame, overlay

def main():
    #Path to .geojsonl files
    fdir = ".\\Raw_data\\"
    fn = [x for x in os.listdir(fdir) if "part" in x]

    #Path to input shapefile
    shx = [os.path.join(".\\Input\\", file) for file in os.listdir(".\\Input\\") if file.endswith(".shp")]
    input_shp = gpd.read_file(shx[0])
    shp_list = input_shp[input_shp.columns[0]].tolist() 

    for j, ID in enumerate(shp_list):
    
        #Make output folder
        fout=".\\Output\\"+ID+"\\" 
        os.makedirs(fout, exist_ok=True)

        #Find intersecting footpirnts with state SHP, export to new SHP
        for i, file in enumerate(fn):
            gdf =  GeoDataFrame.from_file(fdir+file)     
            shp_gdf = input_shp[input_shp[input_shp.columns[0]] == ID].to_crs(gdf.crs) 
            shp_gdf = shp_gdf.drop(columns=shp_gdf.columns[0]) 
            intersection_gdf = overlay(gdf, shp_gdf, how='intersection')
            del gdf
            del shp_gdf

            if len(intersection_gdf) > 0:
                intersection_gdf.to_file(fout+file.replace(".geojsonl","_"+ID+".shp"), driver='ESRI Shapefile')
                del intersection_gdf
            
            else:
                del intersection_gdf
            
            print (ID+": "+str(i+1)+"/"+str(len(fn))+" processed.")
            
        #Merge all shapefiles
        file = os.listdir(fout) 
        path = [os.path.join(fout, i) for i in file if ".shp" in i] 
        gdf1 = gpd.GeoDataFrame(pd.concat([gpd.read_file(i) for i in path], ignore_index=True), crs=gpd.read_file(path[0]).crs)
        gdf1.to_file(os.path.join(fout,"Building_Footprint_"+ID+".shp"), driver='ESRI Shapefile')
        
        del gdf1
        #Delete "split" shapefiles, keep only merged shapefiles
        del_path = [os.path.join(fout, i) for i in file if "part" in i]
        for del_file in del_path:
            os.remove(del_file)
        
        print(ID+" building footprint shapefile generated.")

if __name__ == "__main__":
    main()
