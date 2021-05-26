from flask import Flask, redirect, url_for, render_template ,request ,jsonify ,make_response
import pandas as pd
import geopandas
from pandas import DataFrame

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/findaddress', methods=['GET','POST'])
def findaddress():
    
    req = request.get_json()
    # test
    #ar= [[6.98899,100.20831],[7.10658,100.05704],[7.23755,100.59734],[8.50352,98.58305]]
    ar=req
    df = DataFrame(ar,columns=['lat','lng'])
    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.lng, df.lat))
    gdf.set_crs(epsg=4326, inplace=True)
    countries_gdf = geopandas.read_file("data/tambon.gpkg", layer='tambon',crs={'init': 'epsg:4326'})
    ide = geopandas.overlay( gdf,countries_gdf, how='identity')
    print(req)
    #res = make_response(jsonify({"message": "OK"}), 200)
    #res = make_response(jsonify(req), 200)
    j=ide.to_json()
    print(j)
    res = make_response(j, 200)
    return res

if __name__ == "__main__":
    app.run(debug=True)
