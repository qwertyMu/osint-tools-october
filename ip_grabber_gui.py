import gradio as gr
import requests
import webbrowser

# Function to get geolocation from IP address using a free geolocation API
def get_geolocation(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        data = response.json()
        if 'latitude' in data and 'longitude' in data:
            return data['latitude'], data['longitude']
        else:
            return None, None
    except Exception as e:
        print(f"Error fetching geolocation for IP {ip}: {e}")
        return None, None

# Function to open Google Maps links for the IP addresses
def open_ip_locations(ips):
    ip_list = [ip.strip() for ip in ips.split(",")]
    
    for ip in ip_list:
        latitude, longitude = get_geolocation(ip)
        if latitude is not None and longitude is not None:
            google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
            webbrowser.open_new_tab(google_maps_url)
        else:
            print(f"Could not resolve location for IP: {ip}")

# Gradio interface
def gradio_interface(ips):
    open_ip_locations(ips)
    return "Opened Google Maps for the provided IP addresses."

demo = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Textbox(lines=2, placeholder="Enter IP addresses separated by commas"),
    outputs="text",
    title="IP Address to Google Maps"
)

demo.launch()