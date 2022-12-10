import streamlit as st
from urllib.request import urlopen
import json
import plotly.express as px

def get_weather_data():
    # Make a request to the OpenWeather API to get the data
    api_key = st.secrets['key']
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=Boston,us&units=imperial&appid=' + api_key
    response = urlopen(url)
    data = json.loads(response.read())
    return data

def main():
    st.title('Weather Prediction App')

    # Get the data from the OpenWeather API
    data = get_weather_data()

    # Extract the relevant data from the API response
    dates = [x['dt_txt'] for x in data['list']]
    temps = [x['main']['temp'] for x in data['list']]
    humidity = [x['main']['humidity'] for x in data['list']]

    # Create a plotly line chart to visualize the data
    fig1 = px.line(x=dates, y=temps, title='Temperature Forecast')
    st.plotly_chart(fig1)

    # Create a plotly scatter plot to visualize the humidity data
    fig2 = px.scatter(x=dates, y=humidity, title='Humidity Forecast')
    st.plotly_chart(fig2)

if __name__ == '__main__':
    main()
