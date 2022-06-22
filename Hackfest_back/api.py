from flask import Flask, redirect, request, jsonify
import osmnx as ox
import json


app=Flask(__name__)
@app.route('/distance', methods=['GET', 'POST'])
def giveInfo():  
    if request.method == 'POST':
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        lng = request_data['lng']
        lat = request_data['lat']

        tags = {'amenity': ['hospital', 'clinic'],
                'building': 'hospital',
                'emergency': 'ambulance_station',
                'contact':'email',
                'facility': 'operating_theatre',
                'facility':'x-ray',
            }
        
        gdf = ox.geometries.geometries_from_point((lng,lat), tags, dist=50000).head(50)   # find the hospital around 5km       
        file = gdf.to_json()
        return jsonify({
            "file": file
        })
    else:
       return jsonify({"message": "Completed Task"})   

if __name__ == '__main__':
    app.run(debug=True)