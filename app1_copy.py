import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import requests
from datetime import datetime
import pytz

# Constants for IP and port
IP_ADDRESS = "44.195.44.28" # Server Ip Address
PORT_STH = 8666 # STH PORT
DASH_HOST = "0.0.0.0"  # Set this to "0.0.0.0" to allow access from any IP

# Function to get sensor data (luminosity, humidity, temperature) from the API
def get_sensor_data(attribute, lastN):
    url = f"http://{IP_ADDRESS}:{PORT_STH}/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:BVP/attributes/{attribute}?lastN={lastN}"
    headers = {
        'fiware-service': 'smart',
        'fiware-servicepath': '/'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        try:
            values = data['contextResponses'][0]['contextElement']['attributes'][0]['values']
            return values
        except KeyError as e:
            print(f"Key error: {e}")
            return []
    else:
        print(f"Error accessing {url}: {response.status_code}")
        return []

# Function to convert UTC timestamps to Lisbon time
def convert_to_lisbon_time(timestamps):
    utc = pytz.utc
    lisbon = pytz.timezone('Europe/Lisbon')
    converted_timestamps = []
    for timestamp in timestamps:
        try:
            timestamp = timestamp.replace('T', ' ').replace('Z', '')
            converted_time = utc.localize(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')).astimezone(lisbon)
        except ValueError:
            # Handle case where milliseconds are not present
            converted_time = utc.localize(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')).astimezone(lisbon)
        converted_timestamps.append(converted_time)
    return converted_timestamps

# Set lastN value
lastN = 20  # Get 20 most recent points at each interval

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Sensor Data Dashboard CP5'),
    dcc.Graph(id='sensor-data-graph'),
    # Store to hold historical data for luminosity, humidity, and temperature
    dcc.Store(id='sensor-data-store', data={'timestamps': [], 'luminosity': [], 'humidity': [], 'temperature': []}),
    dcc.Interval(
        id='interval-component',
        interval=10 * 1000,  # in milliseconds (10 seconds)
        n_intervals=0
    )
])

@app.callback(
    Output('sensor-data-store', 'data'),
    Input('interval-component', 'n_intervals'),
    State('sensor-data-store', 'data')
)
def update_data_store(n, stored_data):
    # Get sensor data
    data_luminosity = get_sensor_data("luminosity", lastN)
    data_humidity = get_sensor_data("humidity", lastN)
    data_temperature = get_sensor_data("temperature", lastN)

    if data_luminosity and data_humidity and data_temperature:
        # Extract values and timestamps
        luminosity_values = [float(entry['attrValue']) for entry in data_luminosity]
        humidity_values = [float(entry['attrValue']) for entry in data_humidity]
        temperature_values = [float(entry['attrValue']) for entry in data_temperature]
        timestamps = [entry['recvTime'] for entry in data_luminosity]

        # Convert timestamps to Lisbon time
        timestamps = convert_to_lisbon_time(timestamps)

        # Append new data to stored data
        stored_data['timestamps'].extend(timestamps)
        stored_data['luminosity'].extend(luminosity_values)
        stored_data['humidity'].extend(humidity_values)
        stored_data['temperature'].extend(temperature_values)

    return stored_data

@app.callback(
    Output('sensor-data-graph', 'figure'),
    Input('sensor-data-store', 'data')
)
def update_graph(stored_data):
    if stored_data['timestamps'] and stored_data['luminosity'] and stored_data['humidity'] and stored_data['temperature']:
        # Create traces for the plot
        trace_luminosity = go.Scatter(
            x=stored_data['timestamps'],
            y=stored_data['luminosity'],
            mode='lines+markers',
            name='Luminosity',
            line=dict(color='orange')
        )
        trace_humidity = go.Scatter(
            x=stored_data['timestamps'],
            y=stored_data['humidity'],
            mode='lines+markers',
            name='Humidity',
            line=dict(color='green')
        )
        trace_temperature = go.Scatter(
            x=stored_data['timestamps'],
            y=stored_data['temperature'],
            mode='lines+markers',
            name='Temperature',
            line=dict(color='red')
        )

        # Create figure
        fig_sensor_data = go.Figure(data=[trace_luminosity, trace_humidity, trace_temperature])

        # Update layout
        fig_sensor_data.update_layout(
            title='Sensor Data Over Time',
            xaxis_title='Timestamp',
            yaxis_title='Sensor Values',
            hovermode='closest'
        )

        return fig_sensor_data

    return {}

if __name__ == '__main__':
    app.run_server(debug=True, host=DASH_HOST, port=8050)
