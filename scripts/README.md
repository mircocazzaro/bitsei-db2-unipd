## Pre-Processing Scripts
This folder contains scripts to process the data in such way that it can be used in the application.

---
## Scripts
- `location_process.ipynb` - This script is used to process the location data.
    
    - Input: `active_buisness` - `crime_data` 
    - Output: `processed files`
    - Description: This script is used to process the location data. It takes the active business and crime data location data, and try to mapped location data to the specific area name in LosAngeles. For achieving this, we used `LADCP` [map](https://ladcp.maps.arcgis.com/apps/View/index.html?appid=6c1e477eb9e8491483aac6fd37a46e53) service, and by exploring the api's we found that they have a webservice which can be used to get data in different formats. we used [`geojson` format](https://services1.arcgis.com/tzwalEyxl2rpamKs/arcgis/rest/services/Community_Planning_Areas__CPA_/FeatureServer/0/query?f=geojson&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&maxRecordCountFactor=2&outSR=102100&resultOffset=0&resultRecordCount=4000&cacheHint=true&quantizationParameters=%7B%22mode%22%3A%22view%22%2C%22originPosition%22%3A%22upperLeft%22%2C%22tolerance%22%3A1.0583354500042235%2C%22extent%22%3A%7B%22xmin%22%3A6359577.620000005%2C%22ymin%22%3A1714641.25%2C%22xmax%22%3A6514633.040000007%2C%22ymax%22%3A1945515.3199999928%2C%22spatialReference%22%3A%7B%22wkid%22%3A102645%2C%22latestWkid%22%3A2229%7D%7D%7D) to get the data. and then convert the `lat` and `lon` to the `EPSG:3857` format, so we used `shapely` library to check if the point is inside the polygon or not.

---
## Running the scripts
### Prerequisites
- Pandas
- Geopandas
- Shapely
- pyproj
- Matplotlib

You can easily install the dependencies using `pip install -r requirements.txt`