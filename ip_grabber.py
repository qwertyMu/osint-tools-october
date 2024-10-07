import requests
from bs4 import BeautifulSoup
import webbrowser

def get_geolocation(ip_address):
    """Get geolocation data from IP-API"""
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve geolocation data for {ip_address}")
        return None

def get_google_maps_link(ip_address):
    """Get Google Maps link from geolocation data"""
    geolocation_data = get_geolocation(ip_address)
    if geolocation_data is not None:
        latitude = geolocation_data['lat']
        longitude = geolocation_data['lon']
        google_maps_url = f"https://www.google.com/maps/@?api=1&map_action=zoom_out&zoom=12&center={latitude},{longitude}"
        return google_maps_url
    else:
        return None

def main():
    ip_address = input("Enter an IP address: ")
    google_maps_link = get_google_maps_link(ip_address)
    if google_maps_link is not None:
        print(f"Google Maps link for {ip_address}:")
        print(google_maps_link)
        webbrowser.open_new_tab(google_maps_link)

if __name__ == "__main__":
    main()