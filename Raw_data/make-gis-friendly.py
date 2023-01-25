import pandas as pd
import geopandas as gpd
from shapely.geometry import shape

def main():
    # this is the name of the geography you want to retrieve. update to meet your needs
    location = 'Malaysia'

    dataset_links = pd.read_csv("https://minedbuildings.blob.core.windows.net/global-buildings/dataset-links.csv")
    greece_links = dataset_links[dataset_links.Location == location]
    for _, row in greece_links.iterrows():
        df = pd.read_json(row.Url, lines=True)
        df['geometry'] = df['geometry'].apply(shape)
        gdf = gpd.GeoDataFrame(df, crs=4326)
        gdf.to_file(f"{row.QuadKey}.geojson", driver="GeoJSON")


if __name__ == "__main__":
    main()