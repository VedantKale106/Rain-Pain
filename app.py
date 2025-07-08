from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from geopy.distance import geodesic

app = Flask(__name__)
load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start = request.form["start"]
        end = request.form["end"]
        time_str = request.form["time"]
        departure_time = datetime.strptime(time_str, "%H:%M")

        try:
            start_coords = get_coords(start)
            end_coords = get_coords(end)
        except:
            return render_template("index.html", error="❌ Could not find coordinates. Check place names.", route_found=False)

        # Route coordinates
        route_url = "https://api.openrouteservice.org/v2/directions/driving-car"
        headers = {"Authorization": ORS_API_KEY}
        params = {
            "start": f"{start_coords[0]},{start_coords[1]}",
            "end": f"{end_coords[0]},{end_coords[1]}"
        }
        res = requests.get(route_url, headers=headers, params=params)
        
        if res.status_code != 200:
            return render_template("index.html", error="❌ Could not find route. Check place names.", route_found=False)
            
        coords = res.json()["features"][0]["geometry"]["coordinates"]

        sampled_points = coords[::max(1, len(coords) // 6)]
        total_dist = 0
        weather_data = []
        has_rain = False
        total_rain_points = 0

        for i, (lon, lat) in enumerate(sampled_points):
            if i > 0:
                total_dist += geodesic(
                    (sampled_points[i - 1][1], sampled_points[i - 1][0]),
                    (lat, lon)
                ).km

            eta = departure_time + timedelta(minutes=int((total_dist / 40) * 60))  # 40 km/h avg
            rain_info = get_weather(lat, lon, eta)
            place_name = reverse_geocode(lat, lon)

            if rain_info["alert"]:
                has_rain = True
                total_rain_points += 1

            weather_data.append({
                "location": place_name,
                "lat": lat,
                "lon": lon,
                "time": eta.strftime("%H:%M"),
                "rain": rain_info["rain"],
                "alert": rain_info["alert"],
                "rain_level": rain_info.get("rain_level", 0)
            })

        # Calculate overall weather theme
        rain_percentage = (total_rain_points / len(weather_data)) * 100 if weather_data else 0
        
        return render_template("index.html", 
                             weather_data=weather_data, 
                             route_found=True, 
                             start=start, 
                             end=end,
                             has_rain=has_rain,
                             rain_percentage=rain_percentage)

    return render_template("index.html", route_found=False)

def get_coords(place):
    url = "https://api.openrouteservice.org/geocode/search"
    headers = {"Authorization": ORS_API_KEY}
    params = {"text": place}
    res = requests.get(url, headers=headers, params=params).json()
    coord = res["features"][0]["geometry"]["coordinates"]
    return coord[0], coord[1]

def reverse_geocode(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json",
        "zoom": 14,
        "addressdetails": 1
    }

    try:
        res = requests.get(url, params=params, headers={"User-Agent": "RainRouteChecker/1.0"}).json()
        address = res.get("address", {})

        # Priority: village > town > suburb > locality > city_district > city
        for key in ["village", "town", "suburb", "locality", "city_district", "city"]:
            if key in address:
                return address[key]

        # Fallback to county or full label if no better match
        return address.get("county") or res.get("display_name", "Unknown")

    except Exception as e:
        print("⚠️ Nominatim error:", e)
        return "Unknown"

def get_weather(lat, lon, eta):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    try:
        res = requests.get(url, params=params).json()
        forecast_list = res.get("list", [])
        
        # Find forecast item closest in time to ETA
        closest_item = None
        min_diff = float("inf")

        for item in forecast_list:
            forecast_time = datetime.utcfromtimestamp(item["dt"])
            time_diff = abs((forecast_time - eta).total_seconds())

            if time_diff < min_diff:
                min_diff = time_diff
                closest_item = item

        if closest_item:
            rain_mm = closest_item.get("rain", {}).get("3h", 0)

            if rain_mm == 0:
                level = "No Rain"
                rain_level = 0
            elif rain_mm <= 1:
                level = "Light Rain"
                rain_level = 1
            elif rain_mm <= 5:
                level = "Moderate Rain"
                rain_level = 2
            else:
                level = "Heavy Rain"
                rain_level = 3

            return {
                "rain": level, 
                "alert": level in ["Moderate Rain", "Heavy Rain"],
                "rain_level": rain_level
            }

        return {"rain": "Unknown", "alert": False, "rain_level": 0}

    except Exception as e:
        print("⚠️ Weather API error:", e)
        return {"rain": "Error", "alert": False, "rain_level": 0}
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
