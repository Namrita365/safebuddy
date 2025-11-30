import requests

def get_location():
    """
    Returns approximate latitude, longitude and Google Maps link
    """
    try:
        response = requests.get("https://ipapi.co/json/").json()
        lat = response.get("latitude")
        lon = response.get("longitude")
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        return lat, lon, maps_link
    except Exception as e:
        return None, None, None
