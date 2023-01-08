# Weather app [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/slevin48/weather_app)


## Deploy Streamlit using Docker

https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker

```
docker build -t weather .
```

```
docker run --rm -it -p 8501:8501 weather
```

![weather](weather.png)