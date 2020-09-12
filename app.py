#imports
from flask import Flask, request, render_template

#init
app = Flask(__name__)

#api
api_key = "notgonnatellyou"

@app.route("/custom")

@app.route("/")
#@app.route("/custom")
def custom():
    return render_template("index.html")
    
@app.route("/", methods=['POST'])
#@app.route("/custom/<units>", methods=['POST'])
def custom_location():
    global api_key

    units = "imperial"
    
    ou = ""
    '''
    if units == "imperial":
        ou = "metric"
    elif units == "metric":
        ou = "imperial"
    '''

    lat = str(request.form['lat'])
    lon = str(request.form['lon'])
    place = ""
    return render_template("custom.html",api_key=api_key,lat=lat,lon=lon,ou=ou,units=units,place=place)

@app.route("/current_location/<units>")
def house(units):

    if units == "imperial":
        ou = "metric"
    elif units == "metric":
        ou = "imperial"

    global api_key
    place = "current_location/"
    lat = "40.013400"
    lon = "-75.277920"
    return render_template("location.html",api_key=api_key,units=units,lat=lat,lon=lon,ou=ou,place=place)


@app.route("/phl/<units>")
def phl(units):
    
    if units == "imperial":
        ou = "metric"
    elif units == "metric":
        ou = "imperial"

    global api_key
    place = "phl/"
    lat = "39.9527237"
    lon = "-75.1635262"
    return render_template("custom.html",api_key=api_key,units=units,lat=lat,lon=lon,ou=ou,place=place)


@app.route("/ny/<units>")
def ny(units):
    
    if units == "imperial":
        ou = "metric"
    elif units == "metric":
        ou = "imperial"

    global api_key
    place = "ny/"
    lat = "40.7127281"
    lon = "-74.0060152"
    return render_template("custom.html",api_key=api_key,units=units,lat=lat,lon=lon,ou=ou,place=place)

@app.route("/boston/<units>")
def boston(units):
    
    if units == "imperial":
        ou = "metric"
    elif units == "metric":
        ou = "imperial"

    global api_key
    place = "ny/"
    lat = "42.3602534"
    lon = "-71.0582912"
    return render_template("custom.html",api_key=api_key,units=units,lat=lat,lon=lon,ou=ou,place=place)

@app.route("/la/<units>")
def la(units):
    
    if units == "imperial":
        ou = "metric"
    elif units == "metric":
        ou = "imperial"

    global api_key
    place = "la/"
    lat = "34.054362"
    lon = "-118.265238"
    return render_template("custom.html",api_key=api_key,units=units,lat=lat,lon=lon,ou=ou,place=place)

@app.route("/sf/<units>")
def sf(units):
    
    if units == "imperial":
        ou = "metric"
    elif units == "metric":
        ou = "imperial"

    global api_key
    place = "sf/"
    lat = "37.7790262"
    lon = "-122.4199061"
    return render_template("custom.html",api_key=api_key,units=units,lat=lat,lon=lon,ou=ou,place=place)

@app.route("/help")
@app.route("/h")
@app.route("/customer_support")
def help():
    return render_template("help.html")

#run app
if __name__ == '__main__':
    #app.run(host='192.168.68.131', port=1146)
    app.run(debug=0,port=1146)
